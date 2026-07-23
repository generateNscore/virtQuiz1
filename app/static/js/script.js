console.log("Ready...");

async function checkCategories_FromServer() {
    const response = await fetch(`${API_BASE_URL}/qgs`);
    const categories = await response.json();
    // console.log('getCategories 성공--', categories);
    if (categories.length === 0) {
        console.log('no categories from FromServer()');
        // 화면을 깨끗이...
        document.querySelector("#tableBody_categories").innerHTML = '';
        document.querySelector("#tableBody_names").innerHTML = '';
    }
    // fillTable_Documents(documents);
    let tableBody = document.querySelector("#tableBody_categories");
    tableBody.innerHTML = '';
    for (let index_r = 0; index_r < categories.length; index_r++) {
        let row = tableBody.insertRow();
        const tmp = categories[index_r];
        let txt = categories[index_r]['category'];
        tmp['category'] = `<input type="button" style="float: left; font-size:12px; padding: 2px;" value="${txt}" onclick="getNames_Category('${txt}');"/>`;
        for (let index_c = 0; index_c < colNames_categories.length; index_c++) {
            row.insertCell(index_c).innerHTML = tmp[colNames_categories[index_c]];
        }
    }
}

async function getNames_Category(category) {
    categoryInput.value = category;
    const response = await fetch(`${API_BASE_URL}/qgs/${category}`);
    const names = await response.json();
    // console.log('after getTransaction_id', names);

    let tableBody = document.querySelector("#tableBody_names");
    tableBody.innerHTML = '';
    for (let index_r = 0; index_r < names.length; index_r++) {
        let row = tableBody.insertRow();
        const tmp = names[index_r];
        let txt = names[index_r]['name'];
        tmp['name'] = `<input type="button" style="float: left; font-size:12px; padding: 2px;" value="${txt}" onclick="getQG_Name('${txt}');"/>`;
        tmp['count'] = names[index_r]['questions'].length;
        for (let index_c = 0; index_c < colNames_names.length; index_c++) {
            row.insertCell(index_c).innerHTML = tmp[colNames_names[index_c]];
        }
    }
}


async function getQG_Name(name) {
    descrInput.value = '';
    typeInput.value = '';
    input1.value = '';
    input2.value = '';
    nameInput.value = name;

    const response = await fetch(`${API_BASE_URL}/qgs_name/${name}`);
    QG = await response.json(); // global 변수

    console.log(QG);
    console.log(Array.isArray(QG['questions']));

    descrInput.value = QG['description'];
    typeInput.value = QG['kind'];
    input1.value = QG['questions'];
    input2.value = QG['answers'];

    document.getElementById("preview").disabled = false;
}


async function saveQG() {
    const qg = {
        'category': categoryInput.value,
        'author': user,
        'created': '2026-07-23',
        'kind':typeInput.value,
        'name': nameInput.value,
        'description':descrInput.value,
        'questions':input1.value,
        'answers':input2.value,
        'used': []
    }

    await fetch(`${API_BASE_URL}/qgs`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(qg)
    })
}

async function preview() {
    const id = QG['id']; // QG는 global 변수로 server에서 갖고 왔음.
    console.log(id);
    // const result = preview_ToServer(id);
    // console.log(result);
    const response = await fetch(`${API_BASE_URL}/qg_preview/${id}`);
    const result = await response.json();
    console.log(result);
}


function deleteQG() {
    const id = QG['id']; // QG는 global 변수로 server에서 갖고 왔음.
    const result = deleteQG_fromTable(id);
    console.log(result);
}

async function deleteQG_fromTable(id) {
    const response = await fetch(`${API_BASE_URL}/qgs/${id}`, {
        method: "DELETE"
    });

    if (!response.ok) {
        alert("삭제 실패");
        return;
    }

    const result = await response.json();
    console.log(result);
    alert("삭제되었습니다.");
}

function newDocument() {

}

function getStudentList() {

}
