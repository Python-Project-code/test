from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql import functions as F

# Create a SparkSession

spark = SparkSession.builder.appName('test').getOrCreate()

# Read CSV file into DataFrame with header
#Escribe un código para leer un archivo CSV con PySpark y mostrar las primeras 5 filas. El archivo se llama `data.csv`.
"""
csv_file_path = ("./data/data.csv")
df = spark.read.csv(csv_file_path,header=True)

df.printSchema()
df.show(5)

"""
#Dado un DataFrame con información de ventas, agrega una nueva columna que calcule el total multiplicando la cantidad por el precio unitario.

data = [(1, "Apple", 5, 3.0),
        (2, "Banana", 10, 1.0),
        (3, "Orange", 8, 2.5)]
columns = ["ID", "Product", "Quantity", "UnitPrice"]
df = spark.createDataFrame(data, columns)


df_with_total = df.withColumn("Total",col("Quantity") * col("UnitPrice"))
df_with_total.show()

# Registra el DataFrame anterior como una tabla SQL y escribe una consulta para obtener los productos cuyo precio total (cantidad * precio unitario) sea mayor a 20.

# Registrar el DataFrame como una tabla SQL

df_with_total.createOrReplaceTempView("Sales")


result = spark.sql(
    """
    SELECT Product, Quantity, UnitPrice, Total
    FROM Sales
    WHERE Total >= 20
"""
)

result.show()


# Otras opciones

result_2 = df_with_total.selectExpr("Product","Quantity","UnitPrice","Total").where("Total >= 20")

result_2.show()


result_filter = df_with_total.filter(col("Total")>= 20 )

result_filter.show()


print("----------")

# Usa `rdd.map()` para convertir una lista de tuplas de (producto, cantidad) en (producto, "Alto") si la cantidad es mayor a 5 o (producto, "Bajo") en caso contrario.

data = [("Laptop", 8), ("Mouse", 3), ("Keyboard", 7), ("Monitor", 4)]

rdd = spark.sparkContext.parallelize(data)

result_rdd = rdd.map(lambda x:(x[0], "Alto" if x[1] > 5 else "Bajo"))

print(result_rdd.collect())


# Usa `rdd.filter()` para quedarte solo con los productos que tienen una cantidad mayor a 5.

result_rdd_2 = rdd.filter(lambda x: x[1] >5) 

print(result_rdd_2.collect())



# Dado un DataFrame de ventas, calcula el total de ventas por producto utilizando `groupBy` y `agg`.



print("-----agregaciones-----")

data = [("Apple", 5), ("Banana", 10), ("Orange", 8), ("Apple", 3)]
columns = ["Product", "Quantity"]
df = spark.createDataFrame(data, columns)


result_df = df.groupby("Product").agg(F.sum("Quantity").alias("TotalSales"))

result_df.show()


# Usando RDD, calcula el promedio de cantidad por producto en una lista de tuplas.


rdd = spark.sparkContext.parallelize(data)

result_rdd_3 = rdd.map(lambda x: (x[0],(x[1],1)))\
                .reduceByKey(lambda a, b: (a[0] + b[0], a[1] + b[1]))\
                .mapValues(lambda x: x[0]/x[1])

print(result_rdd_3.collect())