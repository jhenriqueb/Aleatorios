//Matrizes
                //0        //1      //2         //3
const lista = ['arroz ', 'feijao ', 'marcarrao ', 'carne'];


// Matriz != Objeto
const pessoa = ['Jose', 'Henrique']; //matriz
const pessoa1 = {nome: 'Jose', sobrenome: 'Henrique'}; //objeto

//mostra quantos intens tem
//alert(lista.length)

//adicionar mais um item
pessoa.push(21)
document.getElementById('texto').innerHTML = pessoa

//Metodo JOIN - adiciona algo entre os intens 
document.getElementById('texto2').innerHTML = pessoa.join('-')

//Metodo POP - remover ultimo item da lista
document.getElementById('texto').innerHTML = pessoa.pop()
document.getElementById('texto3').innerHTML = pessoa

//Metodo PUSh - adiciona algo no final da lista
document.getElementById('texto').innerHTML = pessoa.push('Branco')
document.getElementById('texto4').innerHTML = pessoa

//Metodo shift - remove o primeiro da lista
document.getElementById('texto').innerHTML = pessoa.shift()
document.getElementById('texto5').innerHTML = pessoa

//Metodo unshift - adiciona o primeiro da lista
document.getElementById('texto').innerHTML = pessoa.unshift('lindo')
document.getElementById('texto6').innerHTML = pessoa




