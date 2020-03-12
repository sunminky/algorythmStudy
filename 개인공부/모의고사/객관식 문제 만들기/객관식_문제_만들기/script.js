function submit () {
	var checked = document.querySelectorAll("input[type='checkbox']:checked");	//체크된 요소들 전부 찾음
	var arr = new Array();	//새로운 배열을 만듬
	for(var i = 0, idx = 0;i < checked.length;i++){
		arr[idx++] = checked[i].value;	//체크된 요소를 배열에 추가
	}
	fetch('/submit', {
		method: 'POST',	//POST방식으로 전송
		headers: {'Content-Type': 'application/json'},	//JSON데이터임을 암시
		body: JSON.stringify({answers:arr})	//보낼 데이터를 JSON으로 파싱해서 보냄
	})
		.then(res => res.json())
		.then((json) => {
		if(json)	//서버에서 주는 json데이터로 정답여부 확인
			document.querySelector("#result").innerHTML = "정답입니다.";
		else
			document.querySelector("#result").innerHTML = "오답입니다.";
    }
		/*.then(ret => {
			// Update Element
			alert("hello");
		}*/);
};
