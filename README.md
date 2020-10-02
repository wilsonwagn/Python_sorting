# ALGORITMOS RELATIVAMENTE LENTOS:

## 01 Bubble Sort
Neste algoritmo cada elemento da posição i será comparado com o elemento da posição i + 1, ou seja, um elemento da posição 2 será comparado com o elemento da posição 3. Por causa dessa forma de execução, o vetor terá que ser percorrido quantas vezes que for necessária, tornando o algoritmo ineficiente para listas muito grandes.
<p align="center"> <img src="https://www.globalsoftwaresupport.com/wp-content/uploads/2012/07/bubble_gif.gif" width="350" title="hover text"> </p>

## 02 Selection Sort
Este algoritmo é baseado em se passar sempre o menor valor do vetor para a primeira posição (ou o maior dependendo da ordem requerida), depois o segundo menor valor para a segunda posição e assim sucessivamente, até os últimos dois elementos.
<p align="center"> <img src="https://www.globalsoftwaresupport.com/wp-content/uploads/2019/09/ezgif.com-video-to-gif-12.gif" width="350" title="hover text"> </p>

## 03 Insertion Sort
O Insertion sort é um algoritmo simples e eficiente quando aplicado em pequenas listas. Neste algoritmo a lista é percorrida da esquerda para a direita, à medida que avança vai deixando os elementos mais à esquerda ordenados.
<p align="center"> <img src="https://www.globalsoftwaresupport.com/wp-content/uploads/2017/02/ezgif.com-video-to-gif-13-1.gif" width="450" title="hover text"> </p>

## 04 Shell Sort
O shell sort, às vezes chamaado de “ordenação por incrementos diminutos”, melhora a ordenação por inserção ao quebrar a lista original em um número menor de sublistas, as quais são ordenadas usando a ordenação por inserção. A forma única como essas sublistas são escolhidas é a chave para o shell sort. Em vez de quebrar a lista em sublistas de itens contíguos, o shell sort usa um incremento i, às vezes chamado de gap, para criar uma sublista escolhendo todos os itens que estão afastados i itens uns dos outros.
<p align="center"> <img src="https://www.globalsoftwaresupport.com/wp-content/uploads/2017/02/ezgif.com-video-to-gif-13-1.gif" width="450" title="hover text"> </p>

# ALGORITMOS MAIS EFICIENTES:

## 05 Merge Sort
Uma implementação de quicksort eficiente geralmente supera o merge sort, mas, por outro lado, a merge sort é previsível. No sentido de que o quicksort pode ter um tempo de execução quadrático no pior caso.
<p align="center"> <img src="https://www.codesdope.com/staticroot/images/algorithm/merge.gif" width="450" title="hover text"> </p>

## 06 Quick Sort
O Quicksort é o algoritmo mais eficiente na ordenação por comparação. Nele se escolhe um elemento chamado de pivô, a partir disto é organizada a lista para que todos os números anteriores a ele sejam menores que ele, e todos os números posteriores a ele sejam maiores que ele. Ao final desse processo o número pivô já está em sua posição final. Os dois grupos desordenados recursivamente sofreram o mesmo processo até que a lista esteja ordenada.
<p align="center"> <img src="http://www-scf.usc.edu/~zhan468/public/Notes/resources/C411339B79F92499DCB7B5F304C826F4.gif" width="650" title="hover text"> </p>
