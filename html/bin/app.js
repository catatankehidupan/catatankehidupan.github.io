$("body").css("min-height", $(window).height())
$(".markdown").html(marked($("textarea").val()))