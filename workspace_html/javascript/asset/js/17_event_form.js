function log(message) {
    // <div class="log">글씨 출력</div>
    const div = document.createElement('div');
    div.classList.add('log');
    div.innerHTML = message;
    const view = document.querySelector('#view');
    view.prepend(div);
}

window.addEventListener('load', function () {

    const query = document.querySelector('#query');
    query.addEventListener('focus', function () {
        query.style.background = 'plum';
    });

    query.addEventListener('blur', function () {
        query.style.background = '';
    });

    // input: 값이 변경될 때
    query.addEventListener('input', function () {
        log(query.value);

        const r = parseInt(Math.random() * 256);
        const g = parseInt(Math.random() * 256);
        const b = parseInt(Math.random() * 256);
        const a = Math.random();

        query.style.backgroundColor = `rgba(${r},${g},${b},${a})`;

    });

    const form = document.querySelector('#form');
    form.addEventListener('submit', function (evt) {

        // 태그의 기본(고유) 기능을 막아준다.
        evt.preventDefault();

        if (query.value.trim().length < 2) {
            alert('검색어는 두 글자 이상입니다.');
        } else {
            form.submit();
        }
    })

    const parent = document.querySelector('#parent');
    parent.addEventListener('click', function (event) {
        log('부모 클릭');

        // target : 실제 이벤트가 발생한 DOM
        console.log('event.target', event.target);

        // currentTarget : 이벤트가 적용되어 있는 DOM
        console.log('event.currentTarget', event.currentTarget);

        // this
        //      addEventListener 안에서는 event.currentTarget
        //      대부분의 경우 window를 가지고 있다.
        //      그래서 현재 this에 어떤 값이 있는지 알고 있을 때만 쓴다.
        //      arrow 함수의 경우 this === window
        console.log('this', this);
        console.log(this === event.currentTarget);
    })

    const child1 = document.querySelector('#child1');
    child1.addEventListener('click', function (event) {
        // 전달 방지
        // 부모로 전달되는 이벤트 중지
        event.stopPropagation();

        log('자식1 클릭');
    })

    // 1. click된 dom을 출력
    // 2. 지금 클릭 요소에 클래스 chk가 있는지 출력
    // 3. 만약 체크박스 일 때만 value 출력.
    // 4. 제목을 클릭했을 때 제목 출력.
    // 5. 작성자를 클릭하면 속성 writer의 값이 나오게
    // 6. table에 위임하지 않고 tr에 위임.
    // const board = document.querySelector('#board');
    // board.addEventListener('click', function (event) {
    //     console.log(event.target);
    //     console.log(event.target.classList);

    //     // 11_dom.html 참고
    //     if (event.target.classList.contains('chk')) {
    //         log(event.target.value);
    //     }

    //     if (event.target.classList.contains('title')) {
    //         log(event.target.innerText);
    //     }

    //     if (event.target.hasAttribute('writer')) {
    //         log(event.target.innerText);
    //         log(event.target.getAttribute('writer'));
    //     }
    // })

    // 7. 체크를 하면 제목이 출력되게
    const trs = document.querySelectorAll('#board tr');

    for (let tr of trs) {
        tr.addEventListener('click', function (event) {
            console.log(event.target);
            console.log(event.target.classList);

            // 11_dom.html 참고
            if (event.target.classList.contains('chk')) {
                log(event.target.value);
                console.log(event.target);

            }

            if (event.target.classList.contains('title')) {
                log(event.target.innerText);
            }

            if (event.target.hasAttribute('writer')) {
                log(event.target.innerText);
                log(event.target.getAttribute('writer'));
            }
        })

        tr.querySelector('input.chk').addEventListener('click', function (event) {
            event.stopPropagation();

            // console.log(this.parentNode);
            console.log(this.parentNode.parentNode.querySelector('.title').innerText);
        })
    }

    bind_quiz();
})

console.log(this);


function bind_quiz() {


    /*
    문제 1 : 주문과 배송
        주문 정보 : input으로 이름, 주소
        ㅁ 주문 정보와 배송 정보가 같습니다
        배송 정보 : input으로 이름, 주소
        + 체크하면 주문 정보가 배송 정보로 복사
        + 체크 풀면 배송 정보 글씨 지우기
    */

    // html에 <div class="q1"> <input type="text">
    /*
     <div class="q1">
            <input type="text" class="delivery" name="name"><br>
            <input type="text" class="delivery" name="address"><br>
            <input type="checkbox" class="delivery chk">주문 정보와 배송 정보가 같습니다.<br>
    
            <input type="text" class="shipment" name="name"><br>
            <input type="text" class="shipment" name="address"><br>
        </div>
    */

    // 위의 board에서 div로 바뀐 것 뿐이니 q1_name은 필요없다.
    // 또, 체크박스 클릭할 때가 메인.
    // 텍스트가 길어지므로 변수에 담아주기.
    const q1_div = document.querySelector('.q1');

    // 이름.
    let q1_reqName = q1_div.querySelectorAll('.delivery')[0];
    let q1_shipName = q1_div.querySelectorAll('.shipment')[0];

    // 주소.
    let q1_reqAddr = q1_div.querySelectorAll('.delivery')[1];
    let q1_shipAddr = q1_div.querySelectorAll('.shipment')[1];

    // 체크박스
    let q1_chk = q1_div.querySelector('input.chk');

    // 체크박스가 클릭됐을 때,
    q1_chk.addEventListener('click', function () {
        // 일단 console.log 찍어보기. // on -> checkbox는 toggle과 비슷하므로.
        // console.log(q1_chk.value);
        // console.log(q1_chk.checked);
        // console.log(`주문한 사람: ${q1_reqName.value}`);
        // console.log(`주문한 주소: ${q1_reqAddr.value}`);

        if (q1_chk.checked) { // checked일 경우.

            // q1_reqName = q1_div.querySelectorAll('.delivery')[0].value; // 굳이 여기서 .value를 뒤에 붙일 필요는 없을 듯.
            // q1_reqAddr = q1_div.querySelectorAll('.delivery')[1].value;
            q1_shipName.value = q1_reqName.value;
            q1_shipAddr.value = q1_reqAddr.value;
            // q1_shipName = ''; // 얘네는 아래료. 뒤에 value도 덧붙여야 함.
            // q1_shipAddr = '';

        } else { // checked가 아닐 경우.
            // 시행착오
            // q1_reqName = this.parentNode.querySelector('.delivery').hasAttribute('name').value;
            // q1_reqAddr = this.parentNode.querySelector('.delivery').hasAttribute('address').value;
            // q1_reqName = q1_div.querySelectorAll('.delivery')[0].value;
            // q1_reqAddr = q1_div.querySelectorAll('.delivery')[1].value;
            // q1_shipName = q1_reqName; // 배송받을 사람 변수의 value값에 넣어줘야 한다.
            // q1_shipAddr = q1_reqAddr; // 마찬가지로 주소 변수의 value값에 넣어줘야 한다.
            // 하지만 여기까지가 위치조차도 잘못됨. check박스가 체크됐을 때로 옮겨야 함.
            q1_shipName.value = ''; // 비워주기
            q1_shipAddr.value = ''; // 비워주기
        }
    })




    /*
        문제 2 : 로그인창
        로그인 버튼 눌렀을 때
        아이디 / 비밀번호 없으면 빨간 글씨 나오게
        단, 아이디/비밀번호를 쓰고 로그인을 누르면 빨간 글씨 지우기
    */
    /*
    <div class="q2">
         아이디: <input type="text" class="login"><br>
         비밀번호: <input type="password" class="login"><br>
         <br>
         <input type="button" class="login" value="login">;
     </div>
    */

    // querySelectorAll('.login')으로 가져와서 value.trim() == ''일 때
    // innerText = 없는 값 입력하라는 메세지.

    const q2_id = document.querySelectorAll('.login')[0];
    const q2_pw = document.querySelectorAll('.login')[1];
    const q2_loginBtn = document.querySelectorAll('.login')[2];
    const q2_warning = document.querySelector('.warning');

    q2_loginBtn.addEventListener('click', function () {
        if (q2_id.value.trim() == '') {
            q2_warning.innerText = 'ID는 필수 입력값입니다.';
        } else if (q2_pw.value.trim() == '') {
            q2_warning.innerText = 'PW는 필수 입력값입니다.';
        } else {
            q2_warning.innerText = '';
        }

    })

    /*
        문제 3 : 피자 주문
        1. 피자 종류 선택 : select
        - 불고기, 페퍼로니, 포테이토, 치즈, 파인애플, 고르곤졸라
        2. 사이즈 선택 : radio
        - small(18000), medium(20000), large(22000)
        3. 도우 선택 : radio
        - 씬, 고구마, 치즈, 소보로
        4. 토핑 : checkbox
        - 감자(2000), 고구마(2000), 치즈(2500), 베이컨(3000), 옥수수(500), 페페론치노(2500)
        [확인]
        + 문제3-1 : 선택 내역 모두 출력
        + 문제3-2 : 선택 내역과 총액 출력
    */
    /*
    <div class="q3">
         <select class="pizza">
             <option value="1">불고기</option>
             <option value="2">페퍼로니</option>
             <option value="3">새우</option>
             <option value="4">치즈</option>
             <option value="5">파인애플</option>
             <option value="6">고르곤졸라</option>
         </select><br>
         <input type="radio" class="size" name="size" value="1" checked>small(18000)
         <input type="radio" class="size" name="size" value="2">medium(20000)
         <input type="radio" class="size" name="size" value="3">large(22000)
         <br>
         <input type="radio" class="dou" name="dou" value="1" checked>씬
         <input type="radio" class="dou" name="dou" value="2">고구마
         <input type="radio" class="dou" name="dou" value="3">치즈
         <input type="radio" class="dou" name="dou" value="4">소보로
         <br>
         <input type="checkbox" class="toping">감자(2000)
         <input type="checkbox" class="toping">고구마(2000)
         <input type="checkbox" class="toping">치즈(2500)
         <input type="checkbox" class="toping">베이컨(3000)
         <input type="checkbox" class="toping">옥수수(500)
         <input type="checkbox" class="toping">페페론치노(2500)
     </div>
    */

    const q3_div = document.querySelector('.q3');
    const q3_order = document.querySelector('.q3_order');

    // q3_div.addEventListener('click', function () {
    q3_div.addEventListener('click', function (event) { // event 받아와주기
        //  그냥 각각 value로 가져와주면 될 것 같은데?
        // 메뉴라는 배열을 추가 선언하고, select, radio, checkbox 선택한 것들 담고 출력 20260722
        // q3_div.stopPropagation();
        const q3_pizza = document.querySelector('.pizza');
        // const q3_size = document.querySelector('.size');
        const q3_size = document.querySelector('[name=size]:checked');
        // const q3_dou = document.querySelector('.dou');
        const q3_dou = document.querySelector('[name=dou]:checked');
        // const q3_toping = document.querySelectorAll('.toping'); 따로 빼는 게 적합하다 판단.
        const q3_orderBtn = document.querySelector('.btn');

        const q3_topingDiv = document.querySelector('.topingDiv');

        const q3_noToping = q3_topingDiv.querySelector('.noToping');
        const q3_toping = q3_topingDiv.querySelectorAll('.toping');

        let q3_menu = [];

        let q3_topingList = [];

        let q3_totalPrice = 0;
        // let q3_topingFlag = true;

        // 각 요소별로 value값 잘 가져와지는지 출력해보기.
        // console.log(q3_pizza[q3_pizza.value - 1].innerText); // 정상출력
        // console.log(q3_size.value); // radio value값 = 의도대로가 아님.가 아니라 텍스트를 뽑고 싶었는데 애초에 안 되는 거였네
        // console.log(q3_size);
        // console.log(q3_dou.value); // radio value값 = 의도대로가 아님. 사이즈와 동일
        // console.log(q3_dou);
        // console.log(q3_toping); // value = undefined, 당연함. for문 돌려야될 듯.

        q3_menu.push(q3_pizza[q3_pizza.value - 1].innerText);
        q3_menu.push(q3_size.value.split('(')[0]);
        q3_menu.push(q3_dou.value);

        // for (let i = 0; i < q3_toping.length; i++) {
        //     // console.log(event.target); // 확인용.
        //     if (q3_toping[i].checked) { // 몇 번째 항목이 체크돼있는지 검사.
        //         // if (q3_toping[0].checked) { // 토핑없음이 체크돼있을 때
        //         // 다른 걸 체크하면 토핑없음을 체크해제하고 싶다.
        //         // toggle 같은 느낌이니까
        //         // q3_toping[0] 토핑없음이 체크돼있는 상태를 저장할 변수를 따로 만들고 
        //         // console.log를 먼저 찍어보자. !q3_toping[0].value 이런 게 제대로 가져와지는지.
        //         // console.log(!q3_toping[0].value); // 가져와지지 않네 뭐가 문젤까?
        //         // !q3_toping[0] 자체를 console.log 찍어보기.
        //         // console.log(!q3_toping[0]); // false가 가져와진다.
        //         // q3_topingFlag = true;   // 토핑없음 플래그 true 설정.
        //         // flag가 아니라 배열을 주면 어떨까? 20260723
        //         if (q3_toping[0].checked) {
        //             for (let t = 1; t < q3_toping.length; t++) {
        //                 q3_toping[t].checked = false;
        //             }
        //         }
        //         if (event.target.value != '토핑없음') {
        //             q3_toping[0].checked = false;
        //             event.target.checked = true;
        //         }
        //         // if (event.target.checked) {
        //         //     event.target.checked == false;
        //         // }
        //         // q3_toping[1].checked = false;
        //         // q3_toping[2].checked = false;
        //         // q3_toping[3].checked = false;
        //         // q3_toping[4].checked = false;
        //         // q3_toping[5].checked = false;
        //         // q3_toping[6].checked = false;


        //     }
        //     // 아래 코드 for문 안쪽 블럭의 if 그대로 위에 넣고 if문으로 체크할 항목을
        //     // if문으로 한 번 더 체크. 
        //     // for (let t = 1; t < q3_toping.length - 1; t++) {
        //     //     if (q3_toping[t].checked) {
        //     //         q3_topingList.unshift(q3_toping[t]);
        //     //         q3_topingList.pop();
        //     //         console.log(q3_topingList[0]);
        //     //     }
        //     // }
        if (event.target.value != '토핑없음' && q3_noToping.checked) {
            q3_noToping.checked = false;
            // q3_topingText.push(event.target.value);
            // console.log(q3_topingText); // 값 잘 들어가는지 체크
            // console.log(q3_noToping.checked, q3_toping); // if에서 검사할 값 체크
        } else {
            if (event.target.value == '토핑없음' && event.target.checked) { // 클릭하는 시점이어야 함. 그래서 false면 동작이 제대로 안 됨..
                q3_noToping.checked = true;
                // q3_topingText.push(q3_noToping.value);
                // console.log(q3_topingText);
                for (let i = 0; i < q3_toping.length; i++) {
                    q3_toping[i].checked = false;
                }
            } else {
                q3_noToping.checked = false;
            }
        }
        if (q3_noToping.checked) {
            q3_menu.push(q3_noToping.value);
        } else {
            for (let i = 0; i < q3_toping.length; i++) {
                if (q3_toping[i].checked) {
                    q3_menu.push(q3_toping[i].value.split('(')[0]);
                }
            }
        }

        // const q3_order = document.querySelector('.q3_order'); // 밖에 빼는 게 맞겠는데 얜
        q3_order.innerText = q3_menu;
        console.log(q3_menu); // 아직 토핑 추가 전 단계의 메뉴. + 추가함. 
        if (event.target.value == '주문') {
            for (let i = 0; i < q3_toping.length; i++) {
                if (q3_toping[i].checked) {
                    // q3_totalPrice += q3_toping[i].value.split('(')[1].slice(0, q3_toping[i].value.split('(')[1].indexOf(')')); // 문자열이니까 Number로 감싸기.
                    q3_totalPrice += Number(q3_toping[i].value.split('(')[1].slice(0, q3_toping[i].value.split('(')[1].indexOf(')')));
                    // console.log('토핑 가격:', Number(q3_toping[i].value.split('(')[1].slice(0, q3_toping[i].value.split('(')[1].indexOf(')'))));
                }
            }
            // q3_totalPrice += q3_size.value.split('(')[1].slice(0, q3_size.value.split('(')[1].indexOf(')'));
            q3_totalPrice += Number(q3_size.value.split('(')[1].slice(0, q3_size.value.split('(')[1].indexOf(')')));
            // console.log('사이즈 가격:', Number(q3_size.value.split('(')[1].slice(0, q3_size.value.split('(')[1].indexOf(')'))));
            // console.log(q3_totalPrice); // 값 체크
            q3_order.innerHTML += ` 총 결제금액: ${q3_totalPrice}원`;
        }
    })
    // const q3_topingDiv = document.querySelector('.topingDiv');
    // q3_topingDiv.addEventListener('click', function (event) {
    //     const q3_noToping = q3_topingDiv.querySelector('.noToping');
    //     const q3_toping = q3_topingDiv.querySelectorAll('.toping');
    //     const q3_orderBtn = document.querySelector('.btn');
    //     let q3_topingText = [];
    //     // let q3_topingArr = []; // 매순간 초기화.
    //     // q3_topingArr.push(q3_noToping.checked); // null이 들어가네.
    //     // q3_noToping check 여부를 if로 먼저 검사
    //     // if (q3_noToping.checked) {
    //     //     q3_topingArr.push(true); // check돼있으면 true
    //     // } else {
    //     //     q3_topingArr.push(false); // 그렇지 않으면 false
    //     // }

    //     // for (let i = 0; i < q3_toping.length; i++) {
    //     //     // q3_topingArr.push(q3_toping[i].checked); // 얘도 마찬가지겠지 이래도 안 된다고?
    //     //     if (q3_toping[i].checked) {
    //     //         q3_topingArr.push(true);
    //     //     } else {
    //     //         q3_topingArr.push(false);
    //     //     }
    //     // }
    //     // console.log(q3_topingArr); // 의도대로 잘 들어갔는지 체크

    //     // console.log(q3_noToping); // 여기서 계속 에러가 나니까 체크. html 저장을 안 해서 생긴 문제.
    //     if (event.target.value != '토핑없음' && q3_noToping.checked) {
    //         q3_noToping.checked = false;
    //         // q3_topingText.push(event.target.value);
    //         // console.log(q3_topingText); // 값 잘 들어가는지 체크
    //         // console.log(q3_noToping.checked, q3_toping); // if에서 검사할 값 체크
    //     } else {
    //         if (event.target.value == '토핑없음' && event.target.checked) { // 클릭하는 시점이어야 함. 그래서 false면 동작이 제대로 안 됨..
    //             q3_noToping.checked = true;
    //             // q3_topingText.push(q3_noToping.value);
    //             // console.log(q3_topingText);
    //             for (let i = 0; i < q3_toping.length; i++) {
    //                 q3_toping[i].checked = false;
    //             }
    //         } else {
    //             q3_noToping.checked = false;
    //         }
    //     }
    //     // 위의 코드 블럭 굳이 분리해둘 필요가 있었을까? 위에 잘 동작하던 것과 합치면 되는 게 아닌가

    //     // if (q3_noToping.checked) {
    //     //     q3_topingText.push(q3_noToping.value);
    //     // } else {
    //     //     q3_topingText.push(event.target.value);
    //     //     console.log(q3_topingText); // 잘 들어가는지 체크.
    //     // } // 안 들어감. 위에 토핑 선택할 때로 묶자.

    //     // q3_order.innerText = q3_order.innerText + q3_topingText;
    //     // // innerText 같은 거로 넣어주는 걸 아예 메뉴 다 받고 끝낸 뒤 for문 돌리기

    // })


    /*
        문제 4 : 메뉴 선택
        인기상품순, 낮은가격순, 높은가격순, 신상품순, 상품평 많은순
        + 클릭한 것만 굵은 글씨로 유지
    */
    /*
         <div class="q4">
            <input type="button" class="q4 btn" value="인기상품순"></button>
            <input type="button" class="q4 btn" value="낮은가격순"></button>
            <input type="button" class="q4 btn" value="높은가격순"></button>
            <input type="button" class="q4 btn" value="신상품순"></button>
            <input type="button" class="q4 btn" value="상품평 많은순"></button>
        </div>
    */

    // 분기점이 있음. 
    // 1.라디오마냥 하나 체크된 상태에서 다른 것 체크했을 때 빼주기
    // 2.체크박스마냥 각각의 버튼들 모두가 클릭될 때 해당 버튼 bold, 한 번 더 클릭하면 bold 해제.
    // flag 처리해서. 클릭된 것 bold 처리. 한 번 더 클릭되면 bold 빼기.

    // 우선 2번부터 구현해보기.
    const q4_div = document.querySelector('.q4');
    const q4_btn = document.querySelectorAll('.q4 .btn');

    // q4_btn.addEventListener('click', function (event) {
    //     let q4_flag = false; // 라디오마냥 구현되게.
    //     event.target.classList.add('.bold');

    // })
    // q4_div.addEventListener('click', function (event) {
    //     event.stopPropagation();

    //     // 방법1. classList.add, remove, contains 활용
    //     // if classList.contains(활용.) 
    //     // if (event.target.classList.contains('bold')) { // bold 클래스를 가지고 있는 경우. = 클릭됐던 것 체크.
    //     //     event.target.classList.remove('bold'); // 클래스 빼기
    //     // } else {
    //     //     // console.log(event.target.value); // 제대로 타겟팅이 되는지 체크. 체크되므로 주석처리.
    //     //     event.target.classList.add('bold'); // classList.add로 클래스 추가해주기.
    //     //     console.log(event.target.classList);
    //     // }

    //     // 근데 위의 방식? 라디오? 토글로도 표현할 수 있는거지. toggle이 좀 더 짧아질 것.
    //     // 방법2. classList.toggle 활용 

    //     event.target.classList.toggle('bold');

    // })

    // 1.라디오마냥 하나 체크된 상태에서 다른 것 체크했을 때 빼주기
    // 배열로 버튼들 true, false 상태를 담아주고
    // indexOf(true)를 찾고.
    // for문을 돌려서 눌린 버튼 인덱스와 배열 인덱스를 비교,
    // 비교했을 때 같고, true라면 toggle('bold') 처리
    // 아니면 클릭된 버튼 add('bold'), 나머지 버튼들 remove('bold').
    // 없는 걸 빼도 에러나진 않으니.
    q4_div.addEventListener('click', function (event) {
        // let q4_boldArr = [false, false, false, false, false];

        // if (q4_boldArr.indexOf(true) == -1) {
        // event.target.classList.toggle('bold');
        // console.log(q4_btn);
        // console.log(event.target);
        if (event.target.value != undefined) { // 값이 들어갔을 때
            event.target.classList.toggle('bold');
            for (let i = 0; i < q4_btn.length; i++) {
                if (q4_btn[i].classList.contains('bold')) {
                    // if (q4_btn[i].value == event.target.value) {
                    //     // event.target.classList.toggle('bold');
                    // }
                    if (q4_btn[i].value != event.target.value) {
                        q4_btn[i].classList.remove('bold');
                        event.target.classList.add('bold');
                    }
                }
            }
        }
    })


    /*
        문제 5 : Todo List
        할일을 적는 input, 추가 버튼
    
        + 5-1 : 추가버튼 누르면 체크박스와 할일이 하단에 추가된다
        + 5-2 : 개별 삭제 버튼이 있고, 클릭 시 그 줄이 지워진다 (dom.remove())
        + 5-3 : 전체 선택 checkbox가 있고
                전체 선택 체크 시 : 모든 checkbox 체크
                해제 시 : 모든 checkbox 체크 해제
        + 5-4 : 전체 선택 후 하나라도 개별 해제가 되면 전체 선택도 해제
                개별로 모두 체크한 경우 전체 선택도 체크된다
        + 5-5 : 선택 삭제 버튼 클릭 시 선택된 내용만 삭제
        */

    // 일단 div 하나 추가. input, 추가 버튼을 만들어주고.
    // 추가 버튼 누르면 = clicke 이벤트 태워주고.
    // checkbox가 있는데, 두 종류가 있지.
    // 전체 선택 checkbox 이건 위에 input, 추가 버튼 부근에 함께 배치해주면 좋을 것 같고.
    // 개별 체크 선택 박스는 당연히
    // documnet.createElement('input').setAttribute('type="checkbox"')
    // 같은 형식으로 추가해주고. 해당 체크박스와 위에서 적은
    // input의 value를 함께 담아줄 div도 생성되게끔.
    // checkbox 전체 선택 같은 것들은 querySelectorAll을 활용해주는 편이 좋을테니
    // setAttribute에 'class="chk"' 같은 것을 함께 넣어주면서 생성해주면 좋겠지.
    // 하나의 todo = div 하나
    // checkbox, text delete button은 이 div의 자식.

    /*
        <div class="q5">
            <h1>Todo List</h1>
            <input type="text" class="todo" placeholder="할 일을 입력하세요.">
            <button type="button" class='todoAdd' value="추가">추가</button>
            <input type="checkbox" id='selectAll' value="전체 선택">전체 선택
            <button type="button" id="deleteCheckedAll" value="선택 삭제">선택 삭제</button>
        </div>
    */

    const q5_div = document.querySelector('.q5');
    const q5_add = document.querySelector('.todoAdd');
    q5_add.addEventListener('click', function () { // 클릭될 때마다 생성
        // const q5_contDiv = document.createElement('div').classList.add('line'); 한 번에 하려 하면 안 되네.
        const q5_contDiv = document.createElement('div');
        // const q5_todoText = document.querySelector('input').hasAttribute('type="text"'); // 이게 아니라 아래처럼
        // const q5_todoText = document.querySelector('input[type="text"]'); // 조각하기 더 쉽도록 클래스 부여
        const q5_todoText = document.querySelector('.todo'); // 할일 적는 input 필드 선택.
        // console.log(q5_todoText);
        // 흠 근데 굳이 계속 변수를 추가해줄 필요가 있을까. innerHTML로 때려박아도 될 것 같은데.
        q5_contDiv.innerHTML = `
        <input type="checkbox" class="q5 chk">${q5_todoText.value}<button type="button" class="delete" value="삭제">삭제
        `
        q5_div.append(q5_contDiv);

        q5_todoText.value = '';

        if (q5_add.parentNode.querySelector('#selectAll').checked) {
            q5_add.parentNode.querySelector('#selectAll').checked = false;
        }

    })

    q5_div.addEventListener('click', function (event) {
        event.stopPropagation();
        const q5_chk = q5_div.querySelectorAll('.chk'); // 4번 해결을 위해 아래에서 3번 진행 중 선언한 변수 활용.
        let q5_chkArr = []; // 매순간 초기화.
        // console.log(event.target); // 어떤 값들이 타겟으로 잡히는지 테스트
        // event.target.classList.contains('line'); // 접근 방향 수정으로 필요없어짐. 주석처리.
        if (event.target.classList.contains('chk')) { // 라인 개별 checkbox 눌렀을 때.
            // event.target.parentNode.classList.add('checked'); // 체크박스의 부모는 Todo list 전체 div의 자식 중 하나인 해당 line
            // 위 코드는 부적합. 한 번 더 클릭했을 때 빼야 하니까. 두 줄 이상으로 구현해야함.

            // 어디서 봤지? 바로 위 문제 4번. toggle이 적합하다.
            // 뭔가 의도했던대로 동작하지 않는다. console.log 찍어보자. 원인: 위에 기존 코드 주석처리 안 해서
            // console.log(event.target.parentNode);
            event.target.parentNode.classList.toggle('checked'); // toggle처리.

            const q5_allCheck = event.target.parentNode.parentNode.querySelector('#selectAll');
            for (let i = 0; i < q5_chk.length; i++) { // 모든 체크박스의 검사를 위함.
                if (q5_chk[i].checked) { // 체크박스 체크 여부.
                    q5_chkArr.push(true); // 배열에 true를 담는다.
                } else {
                    q5_chkArr.push(false); // 배열에 false를 담는다.
                }
            }
            // console.log(q5_chkArr); // 의도대로 값이 잘 담겼는지 체크.
            // console.log(q5_allCheck); // 의도대로 전체 선택 체크박스를 찾아가고 있는지 체크.
            // if (q5_chk.indexOf(0) != -1) { // false가 담겼을 경우. = check되지 않은 항목이 하나라도 있을 경우.
            // 왜 에러가 나나 했더니 위에서 만든 배열로 변경해주지 않았음.
            // if (q5_chkArr.indexOf(0) != -1) { // if문 조건 반대로 줌.
            if (q5_chkArr.indexOf(false) != -1) { // true, false를 배열에 던져줬을 때
                // 그걸 indexOf 같은 거로 체크할 땐 명확히 해야되는 듯. 아 그렇겠네 문자열 체크하는 거니까.
                // event.target.parentNode.parentNode.querySelector('#selectAll').checked == false;
                // 너무 길어진다. 변수에 담자.
                q5_allCheck.checked = false;
            } else if (q5_chkArr.indexOf(false) == -1) { // 거짓, 미체크 항목이 없을 경우.
                // q5_allCheck.checked = !false; // 될 줄 알고 써봤는데 안 되네.
                // if문 조건 같은 거 적을 때 동작하는 듯. 아니면 잘못 썼거나.
                q5_allCheck.checked = true;
            }
        }
        if (event.target.classList.contains('delete')) { // 라인 개별 삭제 버튼을 눌렀을 때.
            // if (event.target.parentNode.classList.contains('checked')) {
            //     div.remove(classList.contains('checked'));
            // }
            // 얌전히 getquerySelector를 한 번 더 쓰자.
            // 5번에서 querySelectorAll로 변경하고 반복문 돌려야될 부분.
            // const q5_deleteDiv = document.querySelector('.checked'); // 체크된 라인에 해당하는 div 가져오기.
            // q5_deleteDiv.remove();
            // 위 코드보단 아래가 낫겠지 싶은데.
            // 위 코드는 할 일1, 2, 3이 있고 1, 3이 체크돼있을 때 3에서 delete를 눌러도 1이 삭제되니까.
            event.target.parentNode.remove();
        }

        // 왜 안 먹나 했는데 id로 줘놓고 클래스를 가져오려니까 당연히 안 먹지.
        // console.log(event.target);
        if (event.target.value == '전체 선택') { // 전체 선택 버튼 클릭 시.
            const q5_chk = q5_div.querySelectorAll('.chk');
            // console.log(event.target);
            // console.log(q5_chk);
            // 테스트용.
            // toggle처럼 작동하려면 어떻게 해야할까? 전체 선택의 checked를 확인하면 되겠지.
            if (event.target.checked) { // 체크됐을 때.
                for (let i = 0; i < q5_chk.length; i++) {
                    if (q5_chk[i].checked == false) {
                        // q5_chk[i].checked == true; // 등호 하나만.
                        q5_chk[i].checked = true;
                        // q5_chk[i].parentNode.classList.add('checked'); // 얘도 위에 한 것처럼 toggle 처리.
                        q5_chk[i].parentNode.classList.toggle('checked');
                    }
                }
            } else {
                for (let i = 0; i < q5_chk.length; i++) {
                    if (q5_chk[i].checked) {
                        q5_chk[i].checked = false;
                        q5_chk[i].parentNode.classList.toggle('checked');
                    }
                }
            }
        }
        if (event.target.value == '선택 삭제') { // 선택 삭제를 눌렀을 때
            const q5_chk = q5_div.querySelectorAll('.chk'); // 5번 해결을 위해 아래에서 3번 진행 중 선언한 변수 활용.
            for (let i = 0; i < q5_chk.length; i++) {
                if (q5_chk[i].checked) { // 체크돼있는 체크박스일 경우.
                    q5_chk[i].parentNode.remove(); // 체크박스의 부모로 한 번만 올라가면 해당 체크박스를 포함한 div가 나옴.
                }
            }
            const q5_allSelect = event.target.parentNode.querySelector('#selectAll');
            q5_allSelect.checked = false;
        }
    })
    // 5-3까지 함. 5-4부터 이어하기
    // 5-4까지 함. 5-5부터 이어하기. 20260725 18:46
}
// 3번 문제 피자, 5번 자잘한 것 마무리. 20260727