# CSS

#####  - Cascading Style Sheets

> 스타일, 레이아웃 등을 통해 문서(HTML)를 표시하는 방법을 지정하는 언어



- CSS 구문

```css
h1{
    color: blue;
    font-size: 15px;
}
```

![image-20210802205341218](CSS.assets/image-20210802205341218.png)

- CSS 구문은 선택자와 함께 열림
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정



## CSS Selectors

#### 선택자 (Selector)

- HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요하다.
- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  -  자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(pseudo class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

![image-20210802211002017](CSS.assets/image-20210802211002017.png)



- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 모든 항목을 선택
- 아이디 선택자
  - '#' 문자로 시작하며, 해당 아이디가 적용된 모든 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용(Unique)
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



#### CSS 적용 우선순위 (cascading order)

1. 중요도 (Importance)
   - !important
2. 우선 순위 (Specificity)
   - 인라인 > id 선택자 > class 선택자, 속성 선택자, pseudo-class > 요소 선택자, pseudo-element
3.  소스 순서



#### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다

  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.

  - 상속 되는 것 예시

    ex) Text 관련 요소(`font`, `color`, `text-align`), `opacity`, `visibility` 등

  - 상속 되지 않는 것 예시

    ex) Box model 관련 요소(`width`, `height`, `margin`, `padding`, `border`, `box-sizing`, `display`),

    position 관련 요소(`position`, `top / right / bottom / left `, `z-index`)

  

## CSS 단위

#### 크기 단위

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀'을 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - 단, 사용자마다 화면 크기가 다르기 때문에 상대적으로 보임
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
  - 주로 스마트폰이나 테블릿 디바이스의 화면을 일컫는 용어로 사용됨
  - 글자 그대로 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - `vw`, `vh`, `vmin`, `vmas`



## 결합자 (Combinators)

![image-20210802213325417](CSS.assets/image-20210802213325417.png)



![image-20210802213332733](CSS.assets/image-20210802213332733.png)

![image-20210802213340240](CSS.assets/image-20210802213340240.png)





## Box model

- 모든 HTML 요소는 box 형태로 되어있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
  - content
  - padding
  - border
  - margin

![image-20210802213500759](CSS.assets/image-20210802213500759.png)



![image-20210802213544207](CSS.assets/image-20210802213544207.png)

![image-20210802213558253](CSS.assets/image-20210802213558253.png)





![image-20210802213613628](CSS.assets/image-20210802213613628.png)

![image-20210802213630339](CSS.assets/image-20210802213630339.png)

#### box-sizing

- 기본적으로 모든 요소의 `box-sizing` 은 `content-box`
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 `box-sizing`을 `border-box`으로 설정

![image-20210802213808798](CSS.assets/image-20210802213808798.png)

#### 마진 상쇄

> block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중에서 큰 마진 값으로 결합(겹쳐지게)되는 현상

![image-20210802215207747](CSS.assets/image-20210802215207747.png)

- 마진 상쇄를 피하기 위해 보통 한 한방향의 마진만 값을 줌

  ex) 모든 박스들이 margin.top = 30px, margin.bottom = 0px 







































