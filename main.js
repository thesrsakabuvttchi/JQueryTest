$(document).ready(main);

function main()
{
    $("#save").attr("disabled",true)
    $("#change").attr("disabled",true)
    $("#reset").attr("disabled",true)

    $('#Employee_id').change(CheckEid)

    $('#change').click(UpdateValues)
    $('#reset').click(resetvals)
}

function CheckEid()
{   
    if($('#Employee_id').val()=='')
        return
    requestData = {Eid : $('#Employee_id').val()}
    params = $.param(requestData)
    $.get('http://127.0.0.1:5000/api/EmpData?'+params).done(
        function(data)
        {
            data = JSON.parse(data)
            if(data.Eid == null)
            {
                $('#save').attr('disabled',false)
                $('#reset').attr('disabled',false)
                $('#change').attr('disabled',true)

                $('#Employee_name').val('')
                $('#Employee_salary').val(null)
                $('#Employee_hra').val(null)
                $('#Employee_da').val(null)
                $('#Employee_deductions').val(null)
            }
            else
            {
                $('#save').attr('disabled',true)
                $('#reset').attr('disabled',false)       
                $('#change').attr('disabled',false)

                $('#Employee_id').attr('disabled',true)
                
                $('#Employee_name').val(data.Ename)
                $('#Employee_salary').val(data.Esal)
                $('#Employee_hra').val(data.HRA)
                $('#Employee_da').val(data.DA)
                $('#Employee_deductions').val(data.Ded)
            }
        })  
}

function UpdateValues(event)
{
    event.preventDefault()
    reqData = {
        Eid : $('#Employee_id').val(),
        Esal : $('#Employee_salary').val(),
        Ename : $('#Employee_name').val(),
        Ehra : $('#Employee_hra').val(),
        Eda : $('#Employee_da').val(),
        Eded : $('#Employee_deductions').val()
    }
    params = $.param(reqData)
    location.href = ('http://127.0.0.1:5000/api/ChangeData?'+params);
}

function resetvals(event)
{
    event.preventDefault()
    $('#Employee_id').attr('disabled',false)
    $('#Employee_id').val('')
    $('#Employee_name').val('')
    $('#Employee_salary').val(null)
    $('#Employee_hra').val(null)
    $('#Employee_da').val(null)
    $('#Employee_deductions').val(null)
    $('#Employee_id').focus()
}