function nextPicture(){
    var pics = ["burger1.png", "burger2.png"];
    

    myImage = document.querySelector('.myImg');
    var index = myImage.getAttribute('index');
    index = (index + 1) % pics.length;
       
    myImage.src = pics[index];
}

function addComment(){
    comments = document.querySelector('.commentList');

    var node = document.createElement('li');
    var textnode = document.createElement('span');
    
    textnode.className = "Username";
    textnode.innerText = 'Dang, that is a good looking burger!';
    
    node.appendChild(textnode);
    comments.appendChild(node);
}