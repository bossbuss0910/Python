class ubcf:
    def usersim(self,data,x,y):
        return 1 - scipy.spatial.distance.cosine(x,y)

    def recommend_calc(self,data):
        for u,i in data.Matrix.items():

