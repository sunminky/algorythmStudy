function submit () {
	var checked = document.querySelectorAll("input[type='checkbox']:checked");
	var arr = new Array();
	for(var i = 0, idx = 0;i < checked.length;i++){
		arr[idx++] = checked[i].value;
	}
	fetch('/submit', {
		method: 'POST',
		headers: {'Content-Type': 'application/json'},
		body: JSON.stringify({answers:arr})
	})
		.then(res => res.json())
		.then((json) => {
        //alert(json); // 서버에서 주는 json데이터가 출력 됨
		if(json)
			document.querySelector("#result").innerHTML = "정답입니다.";
		else
			document.querySelector("#result").innerHTML = "오답입니다.";
    }
		/*.then(ret => {
			// Update Element
			alert("hello");
		}*/);
};
