# MNSIT 정확도 높이 (DNN 학습)

## 1. 학습 횟수에 따른 정확도 변화
3개의 layer, node는 100 -> 64 -> 10
60회까지는 학습횟수가 증가함에 따라 정확도가 증가한다.
하지만 그 이후부터는 증가량이 적거나 낮아진다.

<img width="300px" src="https://user-images.githubusercontent.com/68562176/170721806-a32bd8b5-9a82-422e-bc45-090a4fc91138.jpg">

## 2. 노드 개수에 따른 정확도 변화
노드가 많을수록 정확도가 올라가지만, 1024개가 넘어가면 정확도가 떨어진다.

![Picture2](https://user-images.githubusercontent.com/68562176/170721837-d3226a50-e8e1-46da-956c-aa7686bf2209.jpg)

## 3. 레이어 개수에 따른 정확도 변화
레이어의 개수가 많을수록 정확도가 올라간다. 하지만 9개가 되었을 때는 정확도가 낮아진다.

![Picture3](https://user-images.githubusercontent.com/68562176/170721864-2831b48b-5eef-4e29-9b7d-ebed5acb202f.jpg)

## 가장 높은 정확도
위의 결과들을 토대로 가장 높은 정확도를 만들기 위하여, 아래의 환경에서 실험
>epoch: 60회     
layer: 8개       
output node: 1200 -> 1024 -> 784 -> 512 -> 256 -> 128 -> 64 -> 10   
>
>**정확도: 0. 9799**

<img width="500px" src="https://user-images.githubusercontent.com/68562176/170721898-62ba126b-f863-4b84-b5d7-00078e4a5d9f.jpg">
<img width="500px" src="https://user-images.githubusercontent.com/68562176/170721920-a389b679-986c-469e-b613-c2e9dfcf93aa.jpg">
