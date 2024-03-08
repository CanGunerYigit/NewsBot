import feedparser #linki kullanabilmek için modül
from tkinter import *   #gui ekranımız için modül
import webview 

def open_url(event):  #linkleri tıklanabilir yapmak için fonksiyon yazıyoruz
    webview.create_window(event.widget.cget("text"),event.widget.cget("text")) #tıklanan objenin textini yakala
    webview.start() #başlat


def eskirengedon():
    btndunya.configure(bg="green")    #öncesinde bir butona tıkladığımızda rengini kırmızı yapmıştık şimdi farklı bir butona tıklayınca oda kırmızı olacağı için öncekinin renginin eski haline dönmesi gerek
    btneko.configure(bg="green")       #emin olmak için bu fonksiyon çağırıldığında tüm butonların rengini tekrardan yeşile çekecek
    btnsaglik.configure(bg="green")
    btnson.configure(bg="green")

def temizle():    
    for widget in fhaberler.winfo_children():   #bu fonksiyon herhangi bir haber butonuna tıkladığımızda önceki haberlerin haberler framesinden silinmesini sağlayacak
        widget.destroy() #bulduğun herşeyi yok et


def ortak(haberler):   #tüm butonlarda kullanmak için ortak fonksiyona atadık 
    for haber in haberler.entries: #her habere tek tek ulaşmak için
       Label(fhaberler,text=haber.title,anchor="w",font=('Helveticabold',14)).pack(side=TOP,fill="x") #fhaberlerin içine gelecek ve başlıklara yazdıracak bir label oluşturduk
       lbl_link=Label(fhaberler,text=haber.link,anchor="w",font=('Helveticabold',14),fg="blue",cursor="hand2")#Linkleri yazdıracak yukardakinden ek olarak rengi mavi olacak ve üzerine gelince maus değişecek
       lbl_link.pack(side=TOP,fill="x")
       lbl_link.bind("<Button-1> ",open_url) #Son dakika haberler linkleri tıklanabilir oldu



def son_komut():
    temizle()
    eskirengedon()
    btnson.configure(bg="red") #butona tıkladığımızda rengi değişecek bu sayede hangi sekmede olduğumuzu bileceğiz
    url="https://www.cnnturk.com/feed/rss/all/news" #sondakika haberler url sini alıp değişkene atıyoruz
    haberler=feedparser.parse(url) #az önceki değişkenimizi modülümüzüde kullanabileceğimiz toplu bir değişkene atıyoruz
    ortak(haberler)  #yukarıdaki ortak fonksiyonunu çağırıyoruz
       

def eko_komut():
    temizle()
    eskirengedon() 
    btneko.configure(bg="red") #butona tıkladığımızda rengi değişecek bu sayede hangi sekmede olduğumuzu bileceğiz
    url="https://www.cnnturk.com/feed/rss/ekonomi/news" #ekonomi haberler url sini alıp değişkene atıyoruz
    haberler=feedparser.parse(url) #az önceki değişkenimizi modülümüzüde kullanabileceğimiz toplu bir değişkene atıyoruz
    ortak(haberler) #yukarıdaki ortak fonksiyonunu çağırıyoruz


def saglik_komut():
    temizle()
    eskirengedon() 
    btnsaglik.configure(bg="red") #butona tıkladığımızda rengi değişecek bu sayede hangi sekmede olduğumuzu bileceğiz
    url="https://www.cnnturk.com/feed/rss/saglik/news" #sağlık haberler url sini alıp değişkene atıyoruz
    haberler=feedparser.parse(url) #az önceki değişkenimizi modülümüzüde kullanabileceğimiz toplu bir değişkene atıyoruz
    ortak(haberler) #yukarıdaki ortak fonksiyonunu çağırıyoruz



def dunya_komut():
    temizle()
    eskirengedon() 
    btndunya.configure(bg="red") #butona tıkladığımızda rengi değişecek bu sayede hangi sekmede olduğumuzu bileceğiz
    url="https://www.cnnturk.com/feed/rss/dunya/news" #dünya haberler url sini alıp değişkene atıyoruz
    haberler=feedparser.parse(url) #az önceki değişkenimizi modülümüzüde kullanabileceğimiz toplu bir değişkene atıyoruz
    ortak(haberler) #yukarıdaki ortak fonksiyonunu çağırıyoruz





window =Tk() #bir pencere oluşturduk
window.title("Haberler") #penceremize başlık
window.geometry("1000x600") #penceremize genişlik ve yükseklik verdik


fhaberler=Frame(window,height=600) #haberler için frame oluşturduk windowa eklensin ve yüksekliği 600 olsun
fbutonlar=Frame(window,relief=RAISED,bg="lightblue",bd=2) #butonlar için frame oluşturduk windowa eklenecek kabartmalı stili olacak arkaplan mavi olacak border genişliğimiz 2 olacak

btnson=Button(fbutonlar,text="Son Dakika Haberler",font=('Helveticabold',14),bg="green",command=son_komut) #son dakika haberlerinin butonunu oluşturduk içine yazı, font ve arkaplan rengi ekledik ve buton tetiklendiğinde çalışacak command atadık
btneko=Button(fbutonlar,text="Ekonomi Haberleri",font=('Helveticabold',14),bg="green",command=eko_komut) #ekonomi haberlerinin butonunu oluşturduk içine yazı, font ve arkaplan rengi ekledik ve buton tetiklendiğinde çalışacak command atadık
btnsaglik=Button(fbutonlar,text="Sağlık Haberleri",font=('Helveticabold',14),bg="green",command=saglik_komut) #sağlık haberlerinin butonunu oluşturduk içine yazı, font ve arkaplan rengi ekledik ve buton tetiklendiğinde çalışacak command atadık
btndunya=Button(fbutonlar,text="Dünyadan Haberler",font=('Helveticabold',14),bg="green",command=dunya_komut) #dünya haberlerinin butonunu oluşturduk içine yazı, font ve arkaplan rengi ekledik ve buton tetiklendiğinde çalışacak command atadık

btnson.grid(row=0,column=0,sticky="ew",padx=5,pady=5)  #en üstte sola ve sağa yapışık biçimde x ve y ekseninde 5 birim boşluk konumlansın
btneko.grid(row=1,column=0,sticky="ew",padx=5,pady=5)   #bir alt satır (ekonomi butonu)
btnsaglik.grid(row=2,column=0,sticky="ew",padx=5,pady=5) #bir alt satır (sağlık butonu)
btndunya.grid(row=3,column=0,sticky="ew",padx=5,pady=5) #bir alt satır (dünya butonu)

fbutonlar.grid(row=0,column=0,sticky="ns") #bu sefer yukarı ve aşağıya yapışık bir biçimde ekledik (mavi kolon)
fhaberler.grid(row=0,column=1,sticky="nsew") #fbutonlardan bir birim sağda kalacak ve 4 köşeye yapışık olacak






window.mainloop() #pencere hiç kapanmasın