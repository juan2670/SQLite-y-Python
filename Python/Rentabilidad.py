import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
#Establecer conexión a la base de datos SQLite 
with sqlite3.connect(r'Datos\Northwind.db') as conn:
    # 1. Top 10 productos con mayor rentabilidad 
    query = '''
    select ProductName, SUM(price*quantity) as revenue
    from OrderDetails as od
    join products as p on p.productID = od.productID
    group by od.productID
    order by revenue desc 
    limit 10
    '''
    Top_products = pd.read_sql_query(query,conn)
    #graficamos los resultados
    Top_products.plot(x="ProductName", y="revenue", kind="bar",figsize=(10,5),legend=False)
    plt.title("10 Productos con mayor rentabilidad")
    plt.xlabel("Productos")
    plt.ylabel("Rentabilidad")
    plt.xticks(rotation=45)
    plt.show()
    # 2. obteniendo los empleados mas efectivos es decir los que han realizado mas ventas
    query2 = ''' 
    select FirstName || " " || LastName as Employee, count(*) as total
    from Orders as o
    join Employees as e
    on e.employeeID = o.EmployeeID
    group by o.EmployeeID
    order by total desc
    limit 10
    '''
    #graficamos los resultados
    Top_Employees = pd.read_sql_query(query2,conn)
    Top_Employees.plot(x="Employee",y="total", kind="bar",figsize=(10,5),legend=False)
    plt.title("10 Empleados mas efectivos")
    plt.xlabel("Empleados")
    plt.ylabel("Total vendido")
    plt.xticks(rotation=45)
    plt.show()
       # 3. obteniendo los empleados mas efectivos es decir los que mas han recaudado 
    query3 = '''
        SELECT e.EmployeeID as ID_Empleado, 
        e.FirstName || " " || e.LastName AS nombre_empleados,
        sum(Price * Quantity) as total
        from Orders o 
        join Employees as e
        on e.EmployeeID = o.EmployeeID
        join OrderDetails as od
        on o.OrderID = od.OrderID
        join Products as pr
        on od.ProductID = pr.ProductID
        GROUP by e.EmployeeID, e.FirstName, e.LastName
        order by total DESC
        limit 10
    '''
    #graficamos los resultados
    Top_Employees_Revenue = pd.read_sql_query(query3,conn)
    Top_Employees_Revenue.plot(x="nombre_empleados",y="total", kind="bar",figsize=(10,5),legend=False)
    plt.title("10 Empleados que mas han recaudado")
    plt.xlabel("Empleados")
    plt.ylabel("Total recaudado")
    plt.xticks(rotation=45)
    plt.show()
