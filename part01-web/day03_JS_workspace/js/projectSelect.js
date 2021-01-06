const projects = [
    { pno: "p001", pname: "전자인사관리시스템", pdesc: "기업내 인사정보를 관리하는 시스템" },
    { pno: "p002", pname: "도서관리시스템", pdesc: "기업내 자기개발을 위한 도서대여 시스템" },
    { pno: "p003", pname: "IaaS 서비스", pdesc: "Infa as a Service" },
    { pno: "p004", pname: "PaaS 서비스", pdesc: "Platform as a Service" },
    { pno: "p005", pname: "SaaS", pdesc: "Soft as a Service" },
]

function selectItem() {
    for (i = 0; i < projects.length; i++) {
        //text field data setting
        document.display.pno.value = projects[i].pno;
        document.display.pname.value = projects[i].pname;
        document.display.pdesc.value = projects[i].pdesc;
        break;
    }
}


function displayData() {
    for (i = 0; i < projects.length; i++) {
        document.write("<tr>");
        document.write(``);
        document.write(``);
        document.write("</tr");
    }
}