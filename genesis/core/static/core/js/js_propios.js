$(function(){
	var enlace = $('#link-busqueda');
	enlace.on('click',function(){
		var texto = $('#textob');
		// alert(texto.val())
		enlace.attr('href','http://127.0.0.1:8000/proyectos/lista?duplica=0&criterio=' + texto.val());
		// enlace.attr('href',"{% url 'proyectos:lista' %}" + '?criterio=' + texto);
		// enlace.attr('href','http://www.microsoft.com');
	});
}());

// $(function(){
// 	var fabajo = $("#fabajo");
// 	var farriba = $('#farriba');
// 	var fderecha = $('#fderecha');
// 	var fizquierda = $('#fizquierda');
// 	fabajo.on('click',function(){
// 		alert(fabajo.parent().parent().attr('id'));
// 		name = fabajo.parent().parent().attr('name');
// 		alert(name);
// 		// alert($(this.parent().parent()).attr('id'));
// 		alert('http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + fabajo.parent().parent().attr('id') + '&name=' + name + '&crece=abajo');
// 		fabajo.attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + fabajo.parent().parent().attr('id') + '&name=' + name + '&crece=abajo');
// 	});
// 	farriba.on('click',function(){
// 		name = $(farriba.parent().parent()).attr('name');
// 		farriba.attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' +  $(farriba.parent().parent()).attr('id') + '&name=' + name + '&crece=arriba');
// 	});
// 	fizquierda.on('click',function(){
// 		name = $(fizquierda.parent().parent().parent()).attr('name');
// 		fizquierda.attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + $(fizquierda.parent().parent().parent()).attr('id') + '&name=' + name + '&crece=izquierda');
// 	});
// 	fderecha.on('click',function(){
// 		name = $(fderecha.parent().parent().parent()).attr('name');
// 		fderecha.attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + $(fderecha.parent().parent().parent()).attr('id') + '&name=' + name + '&crece=derecha');
// 	});

// }())

// $(function() {
// 	alert('joa');
//  $(document).on('click', $("[name=fabajo]"), function(event) {
//     let id = this.id;
// 	console.log("Se presionó el Boton con Id :"+ id)
//   });
// });

$( document ).ready(function() {
      // Handler for .ready() called.
    // var element = $('.fiarriba').length; //obtienes el total de elementos dentro del tag ul con clase caja
    var i =0;
    $( ".fiarriba" ).each(function( index ) {
        if ((i >= 0  && i<= 4) || (i>=6 && i<=8) || (i>=10 && i<=11) || i==12 )
        {
            $(this).hide();
        };
        // if (i == 12)
        // {
        //     $(this).attr('src','/static/core/img/abajopequeSF.png');
        // };
        i++;

    });

    i = 0;
    $( ".fiabajo" ).each(function( index ) {
        if ((i >= 1  && i<= 4) || (i>=6 && i<=8) || (i>=9 && i<=11))
        {
            $(this).hide();
        };
        i++;
    });

    i = 0;
    $( ".fiiarriba" ).each(function( index ) {
        if (i >= 0  && i<= 11)
        {
            $(this).hide();
        };
        i++;
    });

    i =0;
    $( ".fiizquierda" ).each(function( index ) {
        // if (i == 5 || i == 9)
        // {
        //     $(this).attr('src','/static/core/img/derechapequeSF.png');
        // };
        if (i==0 || i ==12 || i ==5 || i== 9)
        {
            $(this).hide();
        }
        i++;
    });

    i = 0;
    $( ".fimizquierda" ).each(function( index ) {
        // if (i == 5 || i == 9)
        // {
        //     $(this).attr('src','/static/core/img/derechapequeSF.png');
        // };
        if (i==0 || i ==3 )
        {
            $(this).hide();
        }
        var obj = $("[name=hijos_abajo]");
        if (obj.attr("name") != undefined)
        {
            if (i==6)
            {
                $(this).hide();
            };

        };

        if (obj.attr("name") == undefined)
        {
            if (i==7)
            {
                $(this).hide();
            };

        };

        i++;
    });

    i = 0;
    $( ".fimderecha" ).each(function( index ) {
        // if (i == 5 || i == 9)
        // {
        //     $(this).attr('src','/static/core/img/derechapequeSF.png');
        // };
        // if (i==2 )
        // {
        //     $(this).hide();
        // }
        var obj = $("[name=hijos_abajo]");
        if (obj.attr("name") != undefined)
        {
            // if ( i == 8)
            // {
            //     $(this).hide();
            // };

        };

        if (obj.attr("name") == undefined)
        {
            // if (i==9)
            // {
            //     $(this).hide();
            // };

        };

        i++;
    });


    i=0;
    $( ".fiderecha" ).each(function( index ) {
        // if (i == 4 || i ==11)
        // {
        //     $(this).attr('src','/static/core/img/izquierdapequeSF.png');
        // };
        if ( i ==12 )
        {
            $(this).hide();
        }
        i++;
    });

});


// $( document ).ready(function() {
//     $( "#divpfsc" ).each(function() {
//     $(this).dblclick(function(){
//         alert($(this).attr('class'));
//         alert("Has hecho doble click en el párrafos con id=parrafo");
//     });

//     });
// });

$(document).ready(function(){
    $('div').dblclick(function(){

        const columnas = [['pfpc','colorcolumnaenizquierda'],
                          ['pfsc','colorcolumnalogo'],
                          ['pftc','colorcolumnatitulo'],
                          ['pfcc','colorcolumnalogin'],
                          ['pfqc','colorcolumnaenderecha'],
                          ['sfpc','colorcolumnabumeizquierda'],
                          ['sfsc','colorcolumnabusqueda'],
                          ['sftc','colorcolumnamenu'],
                          ['sfcc','colorcolumnabumederecha'],
                          ['tfpc','colorcolumnamedioizquierda'],
                          ['tfsc','colorcolumnamediocentro'],
                          ['tftc','colorcolumnamedioderecha'],
                          ['cfpc','colorcolumnapie']
                          ];
        var i = 0;
        for (i; i <= 12; i++) {
            if ($(this).attr('name') == columnas[i][0]){
                id = $(this).attr('id');
                window.location.replace('http://127.0.0.1:8000/crear/paleta/?proyecto_id=' + id + '&div=' + columnas[i][1] + '&configuracion_proyecto=proyecto&red=&green=&blue=');
            };        
        }; 


        // if ($(this).attr('name') == 'pfpc'){
        //     id = $(this).attr('id');
        //     window.location.replace('http://127.0.0.1:8000/crear/paleta/?proyecto_id=' + id + '&div=colorcolumnaenizquierda&configuracion_proyecto=proyecto&red=&green=&blue=');
        // };
        // if ($(this).attr('name') == 'pfsc'){
        //     id = $(this).attr('id');
        //     window.location.replace('http://127.0.0.1:8000/crear/paleta/?proyecto_id=' + id + '&div=colorcolumnaenizquierda&configuracion_proyecto=proyecto&red=&green=&blue=');
        // };

    });
});

$(".fabajo").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().attr('name');
    id = $(this).parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + id + '&name=' + name + '&crece=abajo');
    //(... rest of your JS code)
});

$(".faarriba").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().attr('name');
    id = $(this).parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + id + '&name=' + name + '&crece=arriba');
    //(... rest of your JS code)
});

$(".farriba").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().attr('name');
    id = $(this).parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + id + '&name=' + name + '&crece=arriba');
    //(... rest of your JS code)
});
$(".fizquierda").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().parent().attr('name');
    id = $(this).parent().parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + id + '&name=' + name + '&crece=izquierda');
    //(... rest of your JS code)
});

$(".fderecha").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().parent().attr('name');
    id = $(this).parent().parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + id + '&name=' + name + '&crece=derecha');
    //(... rest of your JS code)
});

$(".fmizquierda").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().parent().attr('name');
    idmodelo = $(this).parent().parent().parent().attr('id');
    idproyecto = $(this).parent().parent().parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_modelo/?proyecto_id=' + idproyecto + '&modelo_id=' + idmodelo + '&name=' + name + '&crece=izquierda');
    //(... rest of your JS code)
});
$(".fmderecha").on('click', function(event){
    event.stopPropagation();
    event.stopImmediatePropagation();
    // alert('hola');
    // alert($(this));
    name = $(this).parent().parent().parent().attr('name');
    idmodelo = $(this).parent().parent().parent().attr('id');
    idproyecto = $(this).parent().parent().parent().parent().attr('id');
    // alert(name);
    $(this).attr('href','http://127.0.0.1:8000/crear/conf_modelo/?proyecto_id=' + idproyecto + '&modelo_id=' + idmodelo + '&name=' + name + '&crece=derecha');
    //(... rest of your JS code)
});

// $('#fabajo').on("click",function(){
//   var usersid =  $(this).attr("id");
//   alert(usersid);
//   //post code
// });

    // $(function(){
    //     $('body').on('click', '#fabajo', function(event){
    //         event.preventDefault();
    //         var id = $(this).attr('id'); /* ID del elemento al que se le ha hecho "click" */
    //         name = $(this).parent().parent().attr("name");
    //         alert(name);
    //         // alert(name);
    //         var fabajo = $(this);
    //         alert(fabajo.attr('href'));
    //         alert('http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + $(this).parent().parent().attr('id') + '&name=' + name + '&crece=abajo');
    //         fabajo.attr('href','http://127.0.0.1:8000/crear/conf_base_nueva/?proyecto_id=' + $(this).parent().parent().attr('id') + '&name=' + name + '&crece=abajo');
    //     });
    // });
    // $(function(){
    //     $('body').on('click', '#farriba', function(event){
    //         event.preventDefault();
    //         var id = $(this).attr('id');  ID del elemento al que se le ha hecho "click" 
    //         alert($(this).parent().parent().attr("name"));
    //         // alert($(this).parent().parent().parent().attr('name');
    //     });
    // });

    // $(function(){
    //     $('body').on('click', '#fderecha', function(event){
    //         event.preventDefault();
    //         var id = $(this).attr('id'); /* ID del elemento al que se le ha hecho "click" */
    //         alert($(this).parent().parent().parent().attr("name"));
    //         // alert($(this).parent().parent().parent().attr('name');
    //     });
    // });
    // $(function(){
    //     $('body').on('click', '#fizquierda', function(event){
    //         event.preventDefault();
    //         var id = $(this).attr('id'); /* ID del elemento al que se le ha hecho "click" */
    //         alert($(this).parent().parent().parent().attr("name"));
    //         // alert($(this).parent().parent().parent().attr('name');
    //     });
    // });


// Insertar codigo en ckeditor

function InsertHTML()
{
   // Get the editor instance that we want to interact with.
   var oEditor = FCKeditorAPI.GetInstance('FCKeditor1') ;

   // Check the active editing mode.
   if ( oEditor.EditMode == FCK_EDITMODE_WYSIWYG )
   {
      // Insert the desired HTML.
      oEditor.InsertHtml( '- This is some <a href="/Test1.html">sample<\/a> HTML -' ) ;
   }
   else
      alert( 'You must be on WYSIWYG mode!' ) ;
}

//////////////////////////////

$.fn.insertAtCaret = function (myValue) {
    myValue = myValue.trim();
    CKEDITOR.instances['idofeditor'].insertText(myValue);
};

/////////////////////////////////////////

// it will remove the existing data in the ckeditor and and it will replace it with 'str' variable content.

function insertIntoCkeditor(str){
    CKEDITOR.instances['editor1'].setData(str);
}

function InsertHTML(HTML)
{
  CKEDITOR.instances['editor1'].insertHtml(HTML);
}

////////////////////////////////////////

CKEDITOR.instance['editor1'].insertElement(str);

///////////////////////////////////////////

// Grab the editor instance in onInit() and save a reference to it:

<CKEditor
    editor={ ClassicEditor }
    data="<p>Hello from CKEditor 5!</p>"
    onInit={ editor => {
        console.log( 'Editor is ready to use!', editor );
    } }
    // ...
/>

// Then, use the editor API to insert the content:

editor.model.change( writer => {
    writer.insertText( 'Plain text', editor.model.document.selection.getFirstPosition() );
} );

////////////////////////////////////////////

// Hello Friends, today I am going to share very small code which is how to insert at cursor in CKEditor. We can insert both html and plain text but here we’re going to see inserting html but if we want to insert text then we just need to call insertText function instead of insertHtml.


// <html>
//     <head>
//         <title>Insert at Cursor in CKEditor</title>
//         <meta charset="UTF-8">
//         <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     </head>
//     <body>
//         <textarea id="content"></textarea>
//         <input id="data" type="text"/>
//         <input id="insert" type="button" value="Insert at Cursor"/>
//         <script src="https://code.jquery.com/jquery-3.4.1.min.js" crossorigin="anonymous"></script>
//         <script src="https://cdn.ckeditor.com/4.5.7/standard/ckeditor.js"></script>
//         <script>
//             CKEDITOR.replace('content');
 
//             function insertContent(html) {
//                 for (var i in CKEDITOR.instances) {
//                     CKEDITOR.instances[i].insertHtml(html);
//                 }
//                 return true;
//             }
 
//             $("#insert").click(function () {
//                 insertContent($("#data").val())
//             });
//         </script>
//     </body>
// </html>


///////////////////////////////////

<zk xmlns:w="client">
  <window border="normal" title="hello" apply="pkg$.TestComposer">
  
    <vlayout>
    
      <ckeditor id='editor'></ckeditor>     
    <button id="btn" label="Insert text at the cursor position in the textbox" />
    </vlayout>
  </window>
  <!-- http://stackoverflow.com/questions/11076975/insert-text-into-textarea-at-cursor-position-javascript -->
  <script>
  <![CDATA[
function insertAtCursor(myValue) {
    for(var i in CKEDITOR.instances) {
        CKEDITOR.instances[i].insertText(myValue);
    }
}    
    ]]>
  </script>
</zk>

///////////////////////////////////////

$.fn.insertAtCaret = function (myValue) {
    myValue = myValue.trim();
    CKEDITOR.instances['idofeditor'].insertText(myValue);
};

// @busquedas