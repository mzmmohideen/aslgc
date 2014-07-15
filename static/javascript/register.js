function save() {
var name = document.getElementById("name").value;
    var all={
name : name,
};

$.ajax({
type: "POST",
url: /events/,
data: {
all: all,
csrfmiddlewaretoken: '{{csrf_token}}',
},

success : function(response){
if (response=='saved'){alert('The Details have been saved successfully')}
console.log(response);
},
});
}