# GIT 101

Mediante GIT podemos comenzar a colaborar en proyectos, realizar seguimiento de cambios y mantener nuestra base de código organizado. Recordemos que el código es la forma en cómo los seres humanos comunicamos a otros seres humanos cómo interactuamos cón máquinas. Entre mas ordenado, mas personas pueden entender cómo funciona y colaborar a la vez.

## Ramas y Rasgos 

GIT funciona con ramas, existe una rama principal, mientras que cada desarrollador trabaja en ramas independientes que se terminan juntando con la rama principal. La idea es tener una rama independiente por cada rasgo nuevo ¿Que es un rasgo? Cualquier adición a la rama principal

![Commits on a branch](https://learn.microsoft.com/es-es/devops/_img/branching_line.png)
## Cómo utilizar VScode para interactuar con Git

Insertar Loom aquí

## Cómo utilizar la interfaz gráfica de Github.com para interactuar con Git

Insertar Loom aquí

![Cómo clonar repositorio Github desde Windows - n4gash](https://i0.wp.com/www.n4gash.com/wp-content/2023/01/Git-with-GitHub-Workflows.png?resize=1203%2C638&ssl=1)

## Repo de Comandos

### 1. Clonar un Repositorio Remoto (`clone`)

Para comenzar a trabajar en un proyecto, es necesario clonar el repositorio remoto en una máquina local. Se utiliza el comando `clone` seguido de la URL del repositorio:

`git clone <URL_del_repositorio>` 

Esto creará una copia del repositorio en la máquina local y configurará automáticamente un enlace al repositorio remoto.

### 2. Agregar Cambios al Área de Trabajo (`add`)

Una vez que se hayan realizado cambios en los archivos locales, se deben agregar esos cambios al área de trabajo para prepararlos para ser confirmados. Se utiliza el comando `add` seguido del nombre del archivo o el punto (`.`) para agregar todos los archivos modificados:

bash

`git add <nombre_del_archivo>` 

### 3. Confirmar Cambios (`commit`)

Después de agregar los cambios al área de trabajo, se debe confirmar con un mensaje descriptivo utilizando el comando `commit`:

bash

`git commit -m "Mensaje descriptivo aquí"` 

### 4. Enviar Cambios al Repositorio Remoto (`push`)

Una vez se hayan confirmado cambios localmente, se deben enviar al repositorio remoto utilizando el comando `push`:

bash

`git push` 

Esto actualizará el repositorio remoto con tus cambios locales.

### 5. Fusionar Cambios (`merge`)

Dado que estamos trabajando en un proyecto con varios colaboradores se deben fusionar los cambios con los otros cambios del resto de ramas, puedes utilizar el comando `merge`. Primero, cambia a la rama que deseas fusionar y luego ejecuta el comando `merge` seguido del nombre de la rama que deseas fusionar:

bash

`git checkout <nombre_de_la_rama>
git merge <otra_rama>` 

### 6. Obtener Cambios del Repositorio Remoto (`pull`)

Si otros colaboradores han realizado cambios en el repositorio remoto y deseas obtener esos cambios en tu máquina local, se debe utilizar el comando `pull`:


`git pull` 

Esto traerá los últimos cambios del repositorio remoto y los fusionará automáticamente con la rama local.