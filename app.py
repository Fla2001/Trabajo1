import streamlit as st
import pandas as pd
import numpy as np


# IMPORTAR LIBRERIAS DE LAS CLASES

from libreria_funciones_proyecto1 import calcular_roi
from libreria_clases_proyecto1 import Empleado

# =====================================================
# CONFIGURACIÓN GENERAL
# =====================================================

st.set_page_config(page_title="Proyecto Python Fundamentals",layout="wide")

# =====================================================
# SIDEBAR
# =====================================================

menu = st.sidebar.selectbox(
    "Seleccione una sección",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =====================================================
# HOME
# =====================================================

if menu == "Home":
    
    st.title("Proyecto Aplicado en Streamlit")
    st.subheader("Especialización Python for Analytics")
    st.write("Desarrollado por: Flavia Valencia")

    st.markdown("""
    ### Descripción
    Esta aplicación fue desarrollada como parte del Proyecto 1 del módulo Python Fundamentals.

    La aplicación integra:
    - Variables
    - Estructuras de datos
    - Funciones
    - Programación Orientada a Objetos
    - Streamlit
    - NumPy y Pandas

    ### Tecnologías utilizadas
    - Python
    - Streamlit
    - Pandas
    - NumPy
    """)

# =====================================================
# EJERCICIO 1
# =====================================================

elif menu == "Ejercicio 1":

    st.title("Ejercicio 1 - Flujo de Caja")

    st.markdown("""
    Registro de ingresos y gastos usando listas y estructuras de control.
    """)

    # SESSION STATE
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    concepto = st.text_input("Concepto")

    tipo = st.selectbox(
        "Tipo de movimiento",
        ["Ingreso", "Gasto"]
    )

    valor = st.number_input(
        "Valor",
        min_value=0.0,
        step=1.0
    )

    if st.button("Agregar movimiento"):

        movimiento = {
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        }

        st.session_state.movimientos.append(movimiento)

        st.success("Movimiento agregado correctamente")

    # MOSTRAR TABLA
    if st.session_state.movimientos:

        df = pd.DataFrame(st.session_state.movimientos)

        st.dataframe(df)

        ingresos = df[df["Tipo"] == "Ingreso"]["Valor"].sum()
        gastos = df[df["Tipo"] == "Gasto"]["Valor"].sum()

        saldo = ingresos - gastos

        col1, col2, col3 = st.columns(3)

        col1.metric("Ingresos", f"S/ {ingresos:.2f}")
        col2.metric("Gastos", f"S/ {gastos:.2f}")
        col3.metric("Saldo Final", f"S/ {saldo:.2f}")

        if saldo >= 0:
            st.success("Flujo de caja a favor")
        else:
            st.error("Flujo de caja en contra")



# =====================================================
# EJERCICIO 2
# =====================================================

elif menu == "Ejercicio 2":

    st.title("Ejercicio 2 - Registro con NumPy")

    st.markdown("""
    Registro de productos utilizando arrays y DataFrame.
    """)

    if "productos" not in st.session_state:
        st.session_state.productos = []

    producto = st.text_input("Nombre del producto")

    categoria = st.selectbox(
        "Categoría",
        ["Tecnología", "Ropa", "Alimentos", "Otros"]
    )

    precio = st.number_input(
        "Precio",
        min_value=0.0
    )

    cantidad = st.number_input(
        "Cantidad",
        min_value=1
    )

    if st.button("Agregar producto"):

        total = precio * cantidad

        registro = [
            producto,
            categoria,
            precio,
            cantidad,
            total
        ]

        st.session_state.productos.append(registro)

        st.success("Producto agregado")

    if st.session_state.productos:

        array_datos = np.array(st.session_state.productos, dtype=object)

        df = pd.DataFrame(
            array_datos,
            columns=[
                "Producto",
                "Categoría",
                "Precio",
                "Cantidad",
                "Total"
            ]
        )

        st.dataframe(df)

# =====================================================
# EJERCICIO 3
# =====================================================

elif menu == "Ejercicio 3":

    st.title("Ejercicio 3 - Uso de Funciones")

    st.markdown("""
    Cálculo del ROI utilizando una función importada desde una librería externa.
    """)

    if "historial_roi" not in st.session_state:
        st.session_state.historial_roi = []

    ganancia = st.number_input(
        "Ganancia Neta",
        min_value=0.0
    )

    inversion = st.number_input(
        "Inversión",
        min_value=1.0
    )

    if st.button("Calcular ROI"):

        resultado = calcular_roi(
            ganancia_neta=ganancia,
            inversion=inversion
        )

        roi = resultado["roi_pct"]

        st.success(f"ROI calculado: {roi}%")

        historial = {
            "Ganancia": ganancia,
            "Inversión": inversion,
            "ROI %": roi
        }

        st.session_state.historial_roi.append(historial)

    if st.session_state.historial_roi:

        df_historial = pd.DataFrame(st.session_state.historial_roi)

        st.dataframe(df_historial)

# =====================================================
# EJERCICIO 4
# =====================================================

elif menu == "Ejercicio 4":

    st.title("Ejercicio 4 - CRUD con Clases")

    st.markdown("""
    Gestión de empleados utilizando Programación Orientada a Objetos.
    """)

    if "empleados" not in st.session_state:
        st.session_state.empleados = []

    st.subheader("Crear Empleado")

    nombre = st.text_input("Nombre del empleado")

    salario = st.number_input(
        "Salario Base",
        min_value=1.0
    )

    bono = st.number_input(
        "Porcentaje Bono",
        min_value=0.0,
        max_value=100.0
    )

    descuento = st.number_input(
        "Porcentaje Descuento",
        min_value=0.0,
        max_value=100.0
    )

    if st.button("Crear empleado"):

        empleado = Empleado(
            nombre,
            salario,
            bono,
            descuento
        )

        resumen = empleado.resumen()

        st.session_state.empleados.append(resumen)

        st.success("Empleado registrado")

    # MOSTRAR EMPLEADOS
    if st.session_state.empleados:

        df_emp = pd.DataFrame(st.session_state.empleados)

        st.dataframe(df_emp)

        st.subheader("Eliminar empleado")

        nombres = df_emp["nombre"].tolist()

        eliminar = st.selectbox(
            "Seleccione empleado",
            nombres
        )

        if st.button("Eliminar"):

            st.session_state.empleados = [
                emp for emp in st.session_state.empleados
                if emp["nombre"] != eliminar
            ]

            st.success("Empleado eliminado")