import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=[1,2,3,4]
y=[1,4,9,16]

plt.plot(x, y, 'x--b')
plt.axis([0,5,0,17])

# plt.title("x'in karesi")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.show()
####################### Linear plot #########################################
# x=np.linspace(0,5,100)
# plt.plot(x,x,":b", label="linear",color="blue",linewidth="3")
# plt.plot(x,x**2,"or", label="quadratic",linewidth="1")
# plt.plot(x,x**3,"--g", label="cubic",color="green",linewidth="5")


# plt.title("x linear square cube")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.legend(loc="upper left")
# plt.grid(True)
# plt.show()

########################## Stackplot ############################################

# yil = [2011,2012,2013,2014,2015]

# oyuncu1 = [8,10,12,7,9]
# oyuncu2 = [7,12,5,15,21]
# oyuncu3 = [18,20,22,25,19]

# plt.plot([],[],color="y",label="oyuncu1")
# plt.plot([],[],color="r",label="oyuncu2")
# plt.plot([],[],color="b",label="oyuncu3")

# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3, colors=["y","r","b"])
# plt.title("Yıllara göre atılan goller")
# plt.xlabel("yil")
# plt.ylabel("Gol sayısı")
# plt.axis([2011,2016,0,55])
# plt.legend(loc="upper left")
# plt.show()

########################## Pie plot ############################################

# goal_types = 'Penaltı','Kaleye Atılan Şut','Serbest Vuruş'

# goals = [12,35,7]
# colors = ['y','r','b']

# plt.pie(goals,labels=goal_types,colors=colors,shadow=True, explode=(0.05,0.05,0.05),autopct=%1.1f%%) #autopct ile %'ler dilimler üzerine yazılır.
# plt.show()

########################## Subplot ############################################

# x=np.linspace(0,5,50)
# fig,axs=plt.subplots(4)

# axs[0].plot(x,x**-2,":b", label="linear",color="blue")
# axs[0].set_title("x-1/2")
# axs[1].plot(x,x, label="linear",color="blue")
# axs[2].plot(x,x**2,"or", label="quadratic")
# axs[3].plot(x,x**3,"--g", label="cubic",color="green")

# plt.show()
#////////////////////////////////////////////////////////////////
# x=np.linspace(0,5,50)
# fig,axs=plt.subplots(2,2)
# fig.suptitle("TITLE")

# axs[0,0].plot(x,x**-2,":b", label="linear",color="blue")
# axs[0,0].set_title("x-1/2")
# axs[0,1].plot(x,x, label="linear",color="blue")
# axs[1,0].plot(x,x**2,"or", label="quadratic")
# axs[1,1].plot(x,x**3,"--g", label="cubic",color="green")

# plt.show()
####################################################################

# df=pd.read_csv("csv files/nba.csv")

# df=df.drop(["Number"],axis=1).groupby("Team").mean()

# df.head().plot(subplots=True)
# plt.legend()
# plt.show()

######################### Figure Oluşturma ###########################################

# x=np.linspace(-10,9,20)
# y=x**3
# z=x**-2
# fig,axes=plt.subplots(2,1,figsize=(8,5)) #figsize ile pencere boyutu ayarlanabilir.

# figure=plt.figure()

# axes_cube=figure.add_axes([0.1,0.1,0.9,0.8]) #tamamı 1 (%) olarak düşün
# axes_cube.plot(x,y,"b")
# axes_cube.set_xlabel("x")
# axes_cube.set_ylabel("y")
# axes_cube.set_title("title y=x**3")

# axes_square=figure.add_axes([0.6,0.15,0.3,0.3]) #tamamı 1 (%) olarak düşün (x(%),y(%),wide,height)
# axes_square.plot(x,y,"b")
# axes_square.set_xlabel("x")
# axes_square.set_ylabel("z")
# axes_square.set_title("title z=x**-2")
# axes=figure.add_axes([0,0,1,1])
# axes[0].plot(x,z,label="Square")
# axes[1].plot(x,y,label="Cube")
# plt.tight_layout() # başlıkların çakışmasını önlemek için
# axes[0].legend(loc="lower right") 
#or
# axes[0].legend(loc=4)
#fig.savefig("figure.png") #grafiğin  görüntüsünü almak için
# plt.show()

############################ Bar Grafiği ##############################################

# plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

# plt.legend()
# plt.xlabel("Gün")
# plt.ylabel("Mesafe (km)")
# plt.title("Araç Bilgileri")

# plt.show()

#///////////////////////////////////////////////////////////7

# Histogram 
# yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
# yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

# plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)
# plt.xlabel("yaş grupları")
# plt.ylabel("Kişi Sayısı")
# plt.title("Histogram Grafiği")


# plt.show()
