from flask import Flask

app = Flask(__name__)
# Flask bu app uzerinde calisiyor olacak
# endpoinler(// yapi) kullanacaz..
# base url mi endpoint mi diye biulmek lazim..

@app.route('/home')

# api bu route in altina yönlendirielcek. ama suan altinda caliscak bisey yok. o nedenle def ile fonksiyonlar eklemek durumundayim
def index():
    return 'Hello Flask'
app.run(host='localhost', port=5000)

# simdi bu fonksiyonu run edelim
# app.run(host='http://localhost') # nereye baglancagini belirtiyoruz
# ayni amac icin su sekilde de kullanilir
# nodejs 3000 portunu kullanir
# flask baska bir port kullanilir- bu yüzden kullanilmayan bir port kullanalim
