# Math Teacher Mingle with gemma2
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/notebooks/gemma_sprint_notebook.ipynb)


<img src="https://huggingface.co/blog/assets/gemma2/thumbnail.jpg" width ="600" >

---
### Team Member
- 이진우, 김지은, 이나영
---

### 프로젝트 목적
- langchain과 huggingface를 활용한 모델 파인튜닝
- Pretrain된 모델을 이용하여 초,중학생의 수학 선생님 만들기
---

### 프로젝트 개요
![Frame 9](https://github.com/user-attachments/assets/72c0d6b7-bc54-4382-ab78-d82f82aefe07)

---

### 데이터
- 한국어 학습 : [준범님의 koalpaca](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) 
- 수학 파인튜닝 : [수학 데이터(자체 제작)](https://huggingface.co/datasets/Envy1025/mathdata)
---
### 모델
- 컴퓨팅 리소스 한계로 본 프로젝트에서는 상대적으로 작은 크기의 모델 사용
- [gemma-2-2b-bnb-4bit (Unsloth의 gemma-2-2b-bnb-4bit)](https://huggingface.co/unsloth/gemma-2-2b-bnb-4bit)
---
### 파인튜닝
- `Continued Pre-Training`은 사전 학습된 모델을 특정 도메인이나 태스크에 맞춰 추가 학습하는 방법
- 컴퓨팅 리소스에 맞게 다양한 파라미터 조정을 위해 [Unsloth의 UnslothTrainer](https://devocean.sk.com/blog/techBoardDetail.do?ID=166285&boardType=techBlog) 사용
- koalpaca 데이터를 이용하여 한국어 학습을 진행하고 자체 제작 수학 데이터 학습
  
---
### UI 구현 - Chainlit
 
[<img src ="https://github.com/user-attachments/assets/64ca578b-a4f0-4a4f-b876-bce21b5db1a6" width ="600">](https://chainlit.io/)

<img src ="https://github.com/user-attachments/assets/9bcaee06-dbe6-4054-acc1-783dcdb987df" width ="600">
<img src ="https://github.com/user-attachments/assets/8afcbf08-a187-471f-9b66-69c3c460cec0" width ="600">

---

### 결과
- UI구현 단계에서 한국어 지원이 되지 않아서 영어로 구현하였다.
- 컴퓨팅 리소스 부족으로 유의미한 파인튜닝이 불가능했고 실제 모델 성능이 좋지 않았다.
