$( document ).ready(function() {
  $( "form" ).submit(function( event ) {
    $('#currencies').html();
    console.log($('#date').val());
    var requestUrl = "http://api.fixer.io/" + $('#date').val();
    $.ajax({
      url: requestUrl,
      // The name of the callback parameter, as specified by the YQL service
      jsonp: "callback",
      // Tell jQuery we're expecting JSONP
      dataType: "jsonp",
      // Tell YQL what we want and that we want JSON
      data: {
          q: "select title,abstract,url from search.news where query=\"cat\"",
          format: "json"
      },

      // Work with the response
      success: function( response ) {
          console.log( response.rates ); // server response
          var tblHtml = "";
          $.each(response.rates,function(i,val){
              console.log(i + " " + val);
              tblHtml += "<tr><td>"+i+"</td><td>"+val+"</td></tr>";
          });
          $('#currencies').html(tblHtml);
      }
  });
    event.preventDefault();
  });
});
