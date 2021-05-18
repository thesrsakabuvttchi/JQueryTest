$(document).ready(main);

function main()
{
    $.ajax({url : 'http://worldtimeapi.org/api/timezone/Asia/Kolkata',
    
        success: function(result)
        {
            result = new Date(result['unixtime']);
            result = String(result.getHours())+':'+String(result.getMinutes())
            console.log(result)
            $('#AjaxTime').text("Time by AJAX:"+result)
            $('#AjaxProgress').hide()
        },

        error : function(xhr,status,error)
        {
            console.log("ERROR:",error,status)
        }
    });
}
