from mongoengine import *
import datetime

connect('mongoengine',host='localhost', port=27017)

#Modelo
class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateField(default=datetime.datetime.now())

if __name__ == '__main__':
    # post = Post(
    #     title='Ejemplo',
    #     content='Texto de prueba',
    #     author='Eduardo'                #El objeto post debe cumplir con el modelo si el required está en True
    # )

# post.save()
# print(f'Título: {post.title}')
# print(type(Post.objects))
#
# for p in Post.objects:
#     print(p.title)
#     print(p.content)
#     print(p.author)
#
# p_list = Post.objects(author='Octavio')
#
# print(p_list)
# print(type(p_list))
#     post = Post(
#         title='Ejemplo',
#         content='Texto de prueba',
#         author='Eduardo'  # El objeto post debe cumplir con el modelo si el required está en True
#     )

    while True: #Crear objetos con ID nuevo en DB
        post = Post(
            title='Ejemplo',
            content='Texto de prueba',
            #author='Eduardo'  # El objeto post debe cumplir con el modelo si el required está en True
        )
        post.author = input('Ingresa un nombre: ')
        post.title = input('Ingresa un título: ')
        post.content = input('Ingresa un contenido: ')
        post.save()
        op = input("Intro para seguir/ 0 para detener:  ")

