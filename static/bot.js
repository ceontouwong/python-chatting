$(document).ready(function() {
  function addLi(msg){
    $("#history_message").append($("<li></li>").text(msg));
  }
  function addLi_user(msg){
    $("#history_message").append($("<li></li>").text("你说: " + msg));
  }
  function addLi_resp(msg){
    $("#history_message").append($("<li></li>").text(msg));
  }
  var socket = io.connect(location.protocol+ '//' + document.domain + ':'+ location.port);
  socket.on('response', function(res) {
    addLi("Message From Local Server:" + res);
  });
  //$("ul").append("<li>"+ res + "</li>");

  $("#submit").click(function(){
    addLi_user($("#inputbox").val());
    socket.emit('send', $("#inputbox").val());
  })
  socket.on('resp', function(resp){
    addLi_resp(resp);
  })
});
