import twint
import os
import requests

# Obtener el nombre de usuario del perfil de Twitter desde la entrada por teclado
username = input("Ingresa el nombre de usuario del perfil de Twitter: ")

# Configuración de Twint
c = twint.Config()
c.Username = username  # Nombre de usuario del perfil de Twitter ingresado
c.Media = True  # Descargar medios
c.Store_object = True
twint.Config().Username = "hotcarolcosta"
twint.Config().Media = True



# Obtener los enlaces a los medios
# tweets = twint.output.tweets_list
#
# for tweet in tweets:
#     print(tweet)
# media_urls = []

# for tweet in tweets:
#     if 'photos' in tweet:
#         for photo in tweet['photos']:
#             media_urls.append(photo)

# # Crear un directorio para guardar las imágenes con el nombre del usuario
# save_directory = username
# os.makedirs(save_directory, exist_ok=True)
#
# # Descargar las imágenes
# for index, media_url in enumerate(media_urls):
#     response = requests.get(media_url)
#     if response.status_code == 200:
#         with open(f"{save_directory}/image{index + 1}.jpg", 'wb') as f:
#             f.write(response.content)
#             print(f"Imagen {index + 1} descargada en '{save_directory}'")
#     else:
#         print(f"No se pudo descargar la imagen {index + 1}.")
