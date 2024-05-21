# Semana 5

## Python para todos 🐍🐍 y SQL para algunos 💿💿


#### Tabla de Contenido
- [Objetivo Semanal](#sección-1)
- [Metas Semanales](#sección-2)
- [Usos y abusos de la clase](#sección-3)
- [Base de Datos para el Semestre: Spotify Million Playlists - Editada](#sección-4)
- [SQL Estructura](#sección-5)
- [42 preguntas](#sección-6)


	
### 📈[Objetivo Semanal](#sección-1)

El objetivo de la semana es practicar nociones de SQL + seguir familiriandoze con la programación en Python y Jupyter.

> Concepto de una dominada de espalda(máquina en la caneca), adiestrar un perro, o montar moto: Progresiones y Repeticiones

### 📗[Metas Semanales](#sección-2)
 - [ ] Construir consultas en SQL que nos permitan acceder a una base de datos.
 - [ ] Construir métodos que nos permitan comprobar si las consultas son correctas.
 - [ ] Construir gráficos rudimentarios que nos permitan resumir los datos.

### 📈[Usos y abusos de la clase](#sección-3)
 -  [Repo de Datos -> Género en la UE🇪🇺](https://eige.europa.eu/gender-statistics/dgs)

 ### 🎶🎶 [Base de Datos para el Semestre: Spotify Million Playlists - Editada](#sección-4)
 - El [Spotify Million Playlist Challenge](https://research.atspotify.com/2020/09/the-million-playlist-dataset-remastered/) es una estructura de datos interesantisima que contiene metadatos de un millón de listas creadas en Spotify + las canciones que la componen(con sus respectivos metadatos). El objetivo del conjunto de datos es crear un _sandbox_ de algoritmos, abierto al público, en el problema de sistemas de recomendación. ¿Que es un modelo de recomendación? Es el modelo que permite predecir que después de escuchar Peso Pluma en el 99% de los casos el usuario no quiere escuchar Justice, Judas Priest o Disclosure. Para nuestro curso es maravilloso para practicar técnicas de exploración y de análitca básica en conjuntos de datos estructurados.


 ### 📗[¿Cómo funciona SQL?](#sección-5)
![alt text](image.png)

1. FROM + JOIN

Supongamos que queremos obtener todos los detalles de las canciones junto con la información de la lista de reproducción a la que pertenecen.


```
SELECT p.pid, p.name, s.track_name, s.artist_name
FROM Playlists p
JOIN Song s ON p.pid = s.pid
```

2. WHERE

Para filtrar y obtener sólo las listas de reproducción que tienen más de 50 seguidores.


```
SELECT pid, name, num_followers
FROM Playlists
WHERE num_followers > 50
```

3. GROUP BY + HAVING

Si deseas obtener el número de canciones en cada lista de reproducción, pero sólo para aquellas listas que tienen más de 10 canciones.

```
SELECT pid, COUNT(*) as num_songs
FROM Song
GROUP BY pid
HAVING COUNT(*) > 10
```

4. SELECT

Este es un ejemplo básico donde seleccionamos columnas específicas de una tabla.

```
SELECT pid, name, modified_at
FROM Playlists
```

5. ORDER BY

Para obtener todas las listas de reproducción ordenadas por la fecha de modificación más reciente.

```
SELECT pid, name, modified_at
FROM Playlists
ORDER BY modified_at DESC
```

6. LIMIT

Cuando solo quieres obtener un número limitado de registros, por ejemplo, las 10 primeras canciones más recientes.

```
SELECT track_name, artist_name, modified_at
FROM Song
ORDER BY modified_at DESC
LIMIT 10
```


 ### 📗[42 preguntas](#sección-6)
 1. Top 20 de Playlists mas Recientes
 2. Top 10 de Playlists mas largas 
 3. Top 10 de Canciones que mas se repiten
 

