var oldAudio;

var stateID = 0;

$(document).ready(function() {
  $("#sidebarCollapse").on("click", function() {
    $("#sidebar").toggleClass("active");
  });
});

function endAudio() {
  $("#speaker-anim-" + stateID).removeClass("show-gif");
  $("#speaker-anim-" + stateID).addClass("hide-gif");
  $("#span" + stateID).text("Play");
}

function playmusic(id) {
  if (stateID == 0) {
    var audio = document.getElementById("audio" + id);

    oldAudio = audio;

    stateID = id;

    audio.play();

    $("#span" + id).text("Pause");
    $("#speaker-anim-" + id).removeClass("hide-gif");
    $("#speaker-anim-" + id).addClass("show-gif");
  } else if (stateID != id) {
    if (oldAudio.duration > 0 && !oldAudio.paused) {
      oldAudio.pause();
      // oldAudio.currentTime = 0;
      $("#span" + stateID).text("Play");

      $("#speaker-anim-" + stateID).removeClass("show-gif");

      $("#speaker-anim-" + stateID).addClass("hide-gif");

      var audio = document.getElementById("audio" + id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $("#span" + id).text("Pause");
      $("#speaker-anim-" + id).removeClass("hide-gif");
      $("#speaker-anim-" + id).addClass("show-gif");
    } else {
      var audio = document.getElementById("audio" + id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $("#span" + id).text("Pause");
      $("#speaker-anim-" + id).removeClass("hide-gif");
      $("#speaker-anim-" + id).addClass("show-gif");
    }
  } else {
    if (oldAudio.duration > 0 && !oldAudio.paused) {
      oldAudio.pause();
      // oldAudio.currentTime = 0;
      $("#span" + stateID).text("Play");

      $("#speaker-anim-" + stateID).removeClass("show-gif");
      $("#speaker-anim-" + stateID).addClass("hide-gif");
    } else {
      var audio = document.getElementById("audio" + id);

      oldAudio = audio;

      stateID = id;

      audio.play();

      $("#span" + id).text("Pause");
      $("#speaker-anim-" + id).removeClass("hide-gif");
      $("#speaker-anim-" + id).addClass("show-gif");
    }
  }
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

function change_admin(id) {
  var url = $("#user" + id).attr("url-data");

  var csrftoken = getCookie("csrftoken");

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

  var formData = new FormData();

  if (document.getElementById("user" + id).checked) {
    formData.append("action", "1");
    formData.append("id", id);

    $.ajax({
      url: url,
      type: "POST",
      processData: false,
      contentType: false,
      data: formData,
      success: function(data) {
        data = JSON.parse(data);

        if (data["key"] == "0") {
          alert(data["msg"]);
        } else {
          window.location.reload(true);
        }
      }
    });
  } else {
    formData.append("action", "2");
    formData.append("id", id);

    $.ajax({
      url: url,
      type: "POST",
      processData: false,
      contentType: false,
      data: formData,
      success: function(data) {
        data = JSON.parse(data);

        if (data["key"] == "0") {
          alert(data["msg"]);
        } else {
          window.location.reload(true);
        }
      }
    });
  }
}

function triggerModal() {
  $("#exampleModal").modal();
}
