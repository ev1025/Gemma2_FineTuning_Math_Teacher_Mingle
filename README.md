# Math Teacher Mingle with gemma2
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/notebooks/gemma_sprint_notebook.ipynb)


<img src="https://huggingface.co/blog/assets/gemma2/thumbnail.jpg" width ="600" >

---
### Team Member
- 이진우, 김지은, 이나영
---
### 목적
- langchain과 huggingface를 활용한 모델 파인튜닝
- Pretrain된 모델을 이용하여 초,중학생의 수학 선생님 만들기
---
### 데이터 출처
- [준범님의 koalpaca](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) <br>
- [수학 데이터(자체 제작)](https://huggingface.co/datasets/Envy1025/mathdata)
---
### 사용 모델
- 컴퓨팅 리소스 한계로 본 프로젝트에서는 상대적으로 작은 크기의 모델 사용
- [gemma-2-2b-bnb-4bit (Unsloth의 gemma-2-2b-bnb-4bit)](https://huggingface.co/unsloth/gemma-2-2b-bnb-4bit)
---
### 사용 기법
- `Continued Pre-Training`은 사전 학습된 모델을 특정 도메인이나 태스크에 맞춰 추가 학습하는 방법
- 컴퓨팅 리소스에 맞게 다양한 파라미터 조정을 위해 `UnslothTrainer` 사용
- [Continued Pre-Training (Unsloth의 UnslothTrainer)](https://devocean.sk.com/blog/techBoardDetail.do?ID=166285&boardType=techBlog)
---
### UI 구현 - Chainlit
[<img src ="https://github.com/user-attachments/assets/64ca578b-a4f0-4a4f-b876-bce21b5db1a6" width ="600">](https://chainlit.io/)

<img src ="https://github.com/user-attachments/assets/9bcaee06-dbe6-4054-acc1-783dcdb987df" width ="600">
<img src ="https://github.com/user-attachments/assets/8afcbf08-a187-471f-9b66-69c3c460cec0" width ="600">

