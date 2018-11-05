# 학술제


**각자 branch 꼭 생성해주세요. 본인의 branch에 fetch 및 commit을 합니다 **

프로젝트 시작 전, 본인 branch fetch해서 동기화 해주고

일정량 개발을 마치면 본인 branch에 commit하면 됩니다. 

#### **주의 :: 다른 branch를 fetch하면 파일이 사라질 수 있으니 주의해주세요**



모든 개발이 완료되면 New pull request(깃허브 사이트에 있으니 참고) 를 합니다.

base는 병합되어지는 대상(기본적으로 master), compare은 <개발완료한 브랜치> 가 됩니다.



최종 pull request 승인은 모두가 확인 후에, 승인하는 것으로 하겠습니다. 



 # 프로젝트 구조

- Aserver
  - app.py
  - templates
  - css
- Bserver
  - app.py
  - csss
- img
- raspToSerial
- serialToArduino
- Assistant
  - assistant.py

**Aserver**

> A라즈베리파이의 서버 폴더입니다.



**Bserver**

> B라즈베리파이의 서버 폴더입니다.



**Assistant**
> 구글 어시스턴트 폴더입니다.



**raspToSerial**
> 시리얼 파트 폴더입니다.



**serialToArduino**
> 아두이노 파트 폴더입니다.
> 아두이노 자체에 업로드하지만, 명시적으로 모두가 볼 수 있게하고자,
> 이 폴더에 업로드하면 됩니다.



**img**

> 설계디자인을 저장해둔 폴더입니다.
>
> 프로젝트 개발에 사용되는 폴더는 아닙니다.


참고하기 좋은 문서들

* [Flask](https://mooneegee.blogspot.com/2017/10/python-flask.html)
* [Python3](https://wikidocs.net/book/1)
* [requests 와 BeautifulSoup4](https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/)
* [PyMySQL](https://parkminkyu.github.io/python/flask/05-python-flask.html)



* [BootStrap](http://getbootstrap.com/docs/4.1/getting-started/introduction/)
* jinja2   [문서1](http://jinja.pocoo.org/docs/2.10/templates/) [문서2](http://flask.pocoo.org/docs/1.0/templating/)
* [Rachet](http://goratchet.com/components/)
