
#Precisamos utilizar o método "atualizar" para atualizar as informações do perfil?
 
class MyTwitter:
    def __init__(self):
        self.__repositorio = RepositorioUsuarios()
    
    def criar_perfil(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is not None:
            raise PEException(usuario)
        self.__repositorio.cadastrar(perfil)

    def cancelar_perfil(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else:
            perfil.set_ativo(False)


    def tweetar(self, usuario, mensagem):
        perfil = self.__repositorio.buscar(usuario)
        
        if perfil is None or perfil.is_ativo() == False:
            raise PIException(usuario)
        elif len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException(usuario) 
        else:
            tweet = Tweet(usuario, mensagem)
            perfil.add_tweet(tweet)

    def timeline(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None: 
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else: 
            perfil.get_timeline()

    def tweets(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else:
            perfil.get_tweets()

    def seguir(self, usuario_seguido, usuario_seguidor):
        perfil_seguido = self.__repositorio.buscar(usuario_seguido)
        perfil_seguidor = self.__repositorio.buscar(usuario_seguidor)

        if perfil_seguido is None or perfil_seguidor is None:
            raise PIException(usuario)
        elif perfil_seguido.is_ativo() == False or perfil_seguidor.is_ativo() == False:
            raise PDException(usuario)
        else:
            perfil_seguido.add_seguidor(perfil_seguidor)
            perfil_seguidor.add_seguidos(perfil_seguido)


    def numero_seguidores(self, usuario):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None:
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else:
            count = 0
            for seguidor in perfil.seguidores():
                seguidor = self.__repositorio.buscar(seguidor)
                if seguidor is not None and seguidor.is_ativo():
                    count += 1
            return count
    
    def seguidores(self):
        perfil = self.__repositorio.buscar(usuario)

        if perfil is None: 
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else:
            list_seguidores = []
            for seguidor in perfil.seguidores():
                seguidor = self.__repositorio.buscar(seguidor)
                if seguidor is not None and seguidor.is_ativo() == True:
                    list_seguidores.append(seguidor)
            return list_seguidores


    def seguidos(self):
        perfil = self.__repositorio.buscar(usuario)
        
        if perfil is None: 
            raise PIException(usuario)
        elif perfil is not None and perfil.is_ativo() == False:
            raise PDException(usuario)
        else:
            list_seguidos = []
            for seguido in perfil.seguidos():
                seguido = self.__repositorio.buscar(seguido)
                if seguido is not None and seguido.is_ativo() == True:
                    list_seguido.append(seguido)
            return list_seguido