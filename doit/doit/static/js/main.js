document.addEventListener("DOMContentLoaded", dragItem);
let myContent = "this is the variable which  will hold the content";
const my_card = `<div id="task-1" class="task" draggable="true"><div class="card border-light mb-3" style="max-width: 90%">
        <div class="card-header">Header</div>
            <div class="card-body">
            <img src="" alt="">
                <h5 class="card-title">Light card title</h5>
                <p class="card-text">Some quick 
                    example text to build
                    on the card title and make up the
                    bulk of the card's content.
                    ${myContent}
                    </p>
            </div>
        <div class="card-footer">
            <ul class="footer-list">
            
                <li class="ls-item">first </li>
                <li class="ls-item">second </li>
                <li class="ls-item">third</li>
                <li class="ls-item">third</li>

            </ul>
        </div>
    </div></div>`;
let addTask_btn = document.querySelector("#open-popup");
let closeTask = document.getElementById("close-add-task");
let newTask = document.getElementById("hidden-popup");
let newCategory = document.getElementById("new-category");
let closeCategory = document.getElementById("close-category");
let newCategoryForm = document.getElementById("new-category-form");
let saveCategory = $("#save-category");
const add_task = function () {
    new_task_func();
    newTask.classList.add("popup-active");

    console.log("done");
};

const new_category = function () {
    newCategoryForm.classList.add("popup-active");
};

const close_task = function () {
    newTask.classList.remove("popup-active");
    // dragItem();
};
const close_category = function () {
    newCategoryForm.classList.remove("popup-active");
};

addTask_btn.addEventListener("click", add_task);
closeTask.addEventListener("click", close_task);
newCategory.addEventListener("click", new_category);
closeCategory.addEventListener("click", close_category);

let task = document.getElementById("task-1");

let boxes = document.querySelectorAll(".new-task-body");
// let tasks = document.querySelectorAll('.task');
let drag = null;

function dragItem() {
    let items = document.querySelectorAll(".task");
    items.forEach((item) => {
        item.addEventListener("dragstart", function () {
            drag = item;
            item.style.opacity = "0.5";
        });
        item.addEventListener("dragend", function () {
            drag = null;
            item.style.opacity = "1";
        });
        item.addEventListener("dragover", function () {
            // this;style.opacity="30%";
        });
        boxes.forEach((box) => {
            box.addEventListener("dragover", function (e) {
                e.preventDefault();
                this.style.background = "#98ecd7d2";
                // this;style.opacity="70%";
                this.style.color = "#fff";
            });

            box.addEventListener("dragleave", function () {
                this.style.background = "#08ccb2";
                // this.style.background= '#fff068"'
                this.style.color = "#000";
            });

            box.addEventListener("drop", function () {
                this.append(drag);
                this.style.background = "#08ccb2";
                this.style.color = "#000";
            });
        });
    });
}
////////////////////  Show the Task Form     ////////////////
const add_task_btn = document.getElementById("add-task1");
add_task_btn.addEventListener("click", function () {
    document.body.classList.add("popup-active");
});


////////////////////////////    CREATE New CATEGORY Ajax    ////////////////////

$(document).on("submit", "#category-form", function (e) {
    e.preventDefault();
    let form = $("#category-form");

    $.ajax({
        url: '{% url "blog:create_category" %}',
        data: {
            name: $("#category-name").val(),
            desc: $("#category-description").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        type: "POST",
        dataType: "json",
        header: { "X-CSRFToken": "{% csrf_token %}" },
        success: function (response) {
            let success = response["success"];

            let value = response["cat"];
            if (success) {
                console.log(success);
                alert(`Category ${value} has been created`);
            } else {
                alert("Error while creating Category");
            }
        },
        failure: function (error) {
            alert("error occured while calling django view..");
        },
    });
});

document
    .querySelector("#close-add-task")
    .addEventListener("click", function () {
        document.body.classList.remove("popup-active");
    });

/////////////////////////     ajax Get Categories  //////////////////////
let new_task_func = function () {
    let cat_element = $("#cat_input");

    $.ajax({
        header: { "X-CSRFToken": "{% csrf_token %}" },
        // url:'{% url "blog:new_task" %}',
        url: "new-task/",
        type: "GET",
        dataType: "json",
        success: (message) => {
            // console.log(message.cat_list);
            let arr = message.cat_list;
            // console.log(arr);
            creat_cat_selector(arr);
        },
        error: (message) => {
            console.log(message);
        },
    });
};

//  function createSelectCat(choice){
//     let new_select_cat = `<option value="1">${choice}</option>`;
//     cat_selector.innerHTML+=new_select_cat;
//  }

/////////////////////// function to create new Category selector  ////////////////////////

function creat_cat_selector(arr) {
    const cat_selector = document.getElementById("id_tsk_category");
    cat_selector.innerHTML = "";
    cat_selector.innerHTML = `<option value="" selected="">---------</option>`;

    arr.forEach((v) => {
        let new_select_cat = `<option  value="${v.id}">${v["cat_name"]}</option>`;
        cat_selector.innerHTML += new_select_cat;
    });
}

$(document).on("submit", "#create-task", (e) => {
    e.preventDefault();
    let form = $("#create-task");

    $.ajax({
        url: "create-task/",

        data: {
            tsk_header: $("#id_header").val(),
            tsk_title: $("#id_title").val(),
            tsk_category: $("#id_tsk_category").val(),
            tsk_content: $("#id_content").val(),
            end_time: $("#id_end_time").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        type: "POST",
        dataType: "json",
        header: { "X-CSRFToken": "{% csrf_token %}" },

        success: (message) => {
            alert(`New Task ${message.message} created Correctly`);
            // console.log(message);
            
        },
        error: (message) => {
            alert("error");

            console.log(message);
        },
    });
});


/////////////////////// update the task stack //////////



/////////////////// how to use class for creating and refresh the 

class Card {
    constructor(header, title  , category , content , end_date , isfinished , author){
        this.header = header;
        this.title = title;
        this.category = category;
        this.content = content;
        this.published_date = published_date
        this.end_date = end_date;
        this.isfinished = isfinished;
        this.author  = author;
        this.card_html= `<div id="task-1" class="task" draggable="true"><div class="card border-light mb-3" style="max-width: 90%">
        <div class="card-header">${this.header}</div>
            <div class="card-body">
            <img src="" alt="">
                <h5 class="card-title">${this.title}</h5>
                <p class="card-text">${this.content}
                    </p>
            </div>
        <div class="card-footer">
            <ul class="footer-list">
            
                <li class="ls-item"> Author: ${this.author} </li>
                <li class="ls-item">category  ${this.category} </li>
                <li class="ls-item">Finished : ${this.isfinished}</li>
                <li class="ls-item">End date: ${this.end_date}</li>

            </ul>
        </div></div></div>`;
    }
    new_cart(){
        return this.card_html
    }
}

class Card_Stack{
    constructor(jsonObject ) {
        this.data = jsonObject;
        this.header = this.data['tsk_header'];
        this.title = this.data['tsk_title'];
        // this.image = this.data['image'];
        this.category = this.data['tsk_category']['cat_name'];
        console.log(this.category )
        this.content = this.data['tsk_content'];
        this.puplished_date = this.data['tsk_publish_dt'];
        this.end_date = this.data['tsk_end_time'];
        console.log(this.data['tsk_end_time']);
        this.author = this.data['tsk_author']['username']

        console.log(this.author)
        this.isfinished= this.data['tsk_is_finished'];
    }

    card_update(){
        
        
        this.card = new Card( this.header ,this.title ,this.category , this.content , this.published_date , this.end_date , this.isfinished ,this.author)
        // console.log(this.card.card_html)
        return this.card.card_html
    }

}

///////////// get the stack html element 

function update_tasks_bar(){
    const task_stack = document.getElementById('task-stack1');

    console.log("this is ajax")
    $.ajax({
    url:'gh',
    type:"GET",
    dataType:"json",
    
    
    success:(message)=>{
        console.log("thi is success message")
        data  = message['message']

        console.log(data)
 
        data.forEach((v)=>{
            console.log(v)
            const card_stack = new Card_Stack(v); 
            const new_card = card_stack.card_update();
            task_stack.innerHTML+=new_card;
        });
        
        // console.log(new_card["card"]);

        dragItem();
    },
    error:(message)=>{

        alert('this is error')
    },
});
}


/////////////////  element Event listener

const refresh_stack = document.getElementById('create_task');
refresh_stack.addEventListener("click" , function(){
update_tasks_bar();
});
