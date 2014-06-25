function abrirModal(nome)
{
	$('#'+nome).modal('show');
}

function abrirDatepicker(nome)
{
	$('#'+nome).datepicker({
        autoclose: true,
        language: 'pt-BR',
        orientation: "top auto",
        format: "dd/mm/yyyy",
    });
}