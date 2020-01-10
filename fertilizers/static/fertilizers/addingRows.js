function openCity(evt, productname, productid) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
//  tabcontent = document.getElementById("list-of-products").children;
//  for (i = 0; i < tabcontent.length; i++) {
//    tabcontent[i].firstChild.style.display = "none";
//  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementById("list-of-products").children;
  for (i = 0; i < tablinks.length; i++) {
    //tablinks[i].firstChild.className = tablinks[i].className.replace("active", "");
    tablinks[i].querySelector('li a').className = tablinks[i].querySelector('li a').className.replace(" active", "")
  }


  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(productname).style.display = "block";
  evt.currentTarget.className += " active";
  //evt.currentTarget.href = "{% url 'fertilizers:Detail-product' productid %}"

  var main = document.getElementById('main');

  if (!document.getElementById('list-elements')){
    var para = document.createElement("p");
    para.setAttribute("id", "list-elements");
    var node = document.createTextNode("Below are the entries of product "+productname);
    para.appendChild(node);
    main.appendChild(para)
  } else
    {
      var node = document.getElementById('list-elements')
      node.textContent = "Below are the entries of product "+ productname;
    }
  javaproductname = productname;
}

function toggleSidebar(){
   document.getElementById("sidebar").classList.toggle('active');
}