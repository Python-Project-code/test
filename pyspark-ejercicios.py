from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count



spark = SparkSession.builder.appName("SocialMediaAnalysis").getOrCreate()

data = [
    ("Usuario1", "Positivo", 10, 5),
    ("Usuario2", "Negativo", 3, 1),
    ("Usuario3", "Neutro", 7, 0),
    ("Usuario4", "Positivo", 20, 15),
    ("Usuario5", "Negativo", 4, 2),
]

columns = ["Usuario", "Sentimiento", "Likes", "Retweets"]

df = spark.createDataFrame(data, columns)

# 1. Cuenta cuántos comentarios hay por tipo de sentimiento.
comentarios = df.groupBy("Sentimiento").agg(count("Usuario").alias("Comentario"))
comentarios.show()

# 2. Calcula el promedio de "Likes" por sentimiento.
likesSentimientos = df.groupBy("Sentimiento").agg(count("Likes").alias("num_likes"))
likesSentimientos.show()
# 3. Filtra los usuarios con más de 10 "Likes".
usuariosMayor10 = df.filter(col("Likes") > 10)
usuariosMayor10.show()

# 4. Crea una nueva columna "Interacción" sumando "Likes" + "Retweets".
df_interaccion = df.withColumn("Interacción", col("Likes") + col("Retweets"))
df_interaccion.show()

spark.stop()