
document.addEventListener('DOMContentLoaded',comenzar,false);
// window.addEventListener('load', (event) => {
// alert('The page has fully loaded');
// });
var canvas;
var seleccionado;
var nuevo = 1;
var id_proyecto = 140;
var id_modelo = 0;
var json = '';

function comenzar(){

    // Leer los parametros url
    json = document.getElementById('json');
    console.log(json.innerHTML.length);
    var parametrosUrl = new URLSearchParams(window.location.search);
    if (json.innerHTML.length > 0){
        nuevo = 0;
        try {
            // json = parametrosUrl.get('json');
            id_proyecto = parametrosUrl.get('proyecto_id');
            id_modelo = parametrosUrl.get('modelo_id');
            console.log('modeloid entrada:',id_modelo);
            if (json != ''){
                nuevo = 0;
            }else{
                nuevo=1;
            }
        }
        catch{
            nuevo = 1;
        };
    }else{
        nuevo=1;
        id_proyecto = parametrosUrl.get('proyecto_id');
        id_modelo = parametrosUrl.get('modelo_id');
        console.log('modeloid entrada:',id_modelo);
};

    // Recupera las zonas
    if (json.innerHTML != ''){
        var lista = JSON.parse(json.innerHTML).propiedades;
        for (var i in lista){
            // console.log(lista[i]['zonaid']);
            // console.log(lista[i]['propid']);
            // console.log(lista[i]['width']);
            // console.log(lista[i]['left']);
            // console.log(lista[i]['nombre']);
            // console.log(json.title);
            var a = Math.floor(Math.random() * 10000) + 1;
            html = CreaCuadro(lista[i]['zonaid'] + '_' + lista[i]['propid'] + '_' + a,json.title.split(','),lista[i]['width'],lista[i]['nombre'],lista[i]['left'])
            // console.log(html);
            zona = document.getElementById('zona_' + lista[i]['zonaid']);
            // console.log(zona);
            zona.innerHTML += html;
        };
    };
    zonas = document.querySelectorAll('div.zona');
    for (i=0;i<zonas.length;i++){
        zonas[i].addEventListener('dragover', entra_zona,false);
        zonas[i].addEventListener('dragleave', sale_zona,false);
        zonas[i].addEventListener('drop', suelta_zona,false);
        // console.log(zonas[i],zonas[i].id, zonas[i].getAttributeNode("name").value);
    };

    propiedades = document.querySelectorAll('div.propiedad');
    for (i=0;i<propiedades.length;i++){
        propiedades[i].addEventListener('dragstart', inicia_drag,false);
    };

    basurero = document.getElementById('basurero');
    basurero.addEventListener('dragover',entra_basurero,false);
    basurero.addEventListener('drop',suelta_basurero,false);
}

// function inicia_arrastre(e){
//     // e.preventDefault();
//     e.dataTransfer.setData('Text', e.target.getAttribute('name'));
// }

// entra en el canvas

function entra_zona(e){
    e.preventDefault();
    this.style.background = '#29ff00';
}
function sale_zona(e){
    this.style.background = "#FFFFFF";
    e.preventDefault();
}
function inicia_drag(e){
    zonas = document.querySelectorAll('div.zona');
    for (i=0;i<zonas.length;i++){
        zonas[i].style.background = '#ffffff';
    };
    e.dataTransfer.setData("Text", e.target.getAttribute('title'));
}

// {{linea.0}}|{{linea.4}}|{{linea.5}}|{{linea.6}}|{{linea.7}}|{{linea.8}}|{{linea.9}}|{{linea.10}}|{{linea.3}}
// 0 - nombre de propiedad
// 1 - numero de la zona
// 2 - Tipo de propiedad
// 3 - Texto botones
// 4 - Largo string
// 5 - Totaliza
// 6 - Ancho en reporte
// 7 - id del modelo
// 8 - Nombre

function suelta_zona(e){
    e.preventDefault();
    var propiedad = e.dataTransfer.getData('Text');
    atributos = propiedad.split("|");
// encontrar id del modelo en el title de la propiedad
    id_modelo_prop = atributos[7];
    // encontrar el id del modelo en la zona
    id_modelo_zona = this.id.split('_')[1];
    // encontrar el modelo
    modelo = document.getElementById(atributos[7]);
    if (id_modelo_prop == id_modelo_zona){
        var font = modelo.title.split(',');
        // El id del cuadro es: (id del modelo)_(id de la propiedad)_(un random entre 0 y 9000)  
        var a = Math.floor(Math.random() * 10000) + 1;
        var html = CreaCuadro(modelo.id + '_' + atributos[8] + '_' + a,font,atributos[6],atributos[0],0); 
        if (this.innerHTML == ''){
            this.innerHTML = html;
        } else{
            this.innerHTML += html;
        };
        // const parser = new DOMParser();
        // eleHtml = parser.parseFromString(html, 'text/html');
        cuadro = AcomodaCuadro(this);
        this.style.background = '#ffffff';
    }else{
        this.style.background = '#ff0000';
    }
}
function CreaCuadro(id,font,width,nombre,left){
    var cuadro = '<div ondragover="permite_drag_propiedad(event)" ondragstart="muevo_propiedad(event)" onmousedown="que_boton(event,this)" onclick="click_propiedad(this)" id="' + id + '" style="position: absolute; left:0px; font-name:' + font[0] + '; font-size:' + font[1] + 'pt;font-weight:' + font[2] + ';float:left; margin-left:10 px;width:' + width + 'px; left:' + left + 'px;" class="border">' + nombre + '</div>'
    return cuadro;
}
function AcomodaCuadro(zona){
    // Calcula el desplazamiento
    desp = parseInt(zona.childNodes[zona.childNodes.length-2].style.left) + parseInt(zona.childNodes[zona.childNodes.length-2].style.width);
    // encuentra elemento en el innerHTML de la zona
    cuadro = zona.childNodes[zona.childNodes.length-1];
    cuadro.style.left = desp + 'px';
    return cuadro;
}

function click_propiedad(elemento){
}
function que_boton(e,elemento){
    blanquea_propiedades();
    if (e.button == 0){
        elemento.style.background = 'gray';
        seleccionado =  elemento;
    }
}
function muevo_propiedad(e){
    e.dataTransfer.setData("Text", e.target.id);
}
function permite_drag_propiedad(e){
    e.preventDefault();
}
function blanquea_propiedades(){
    zonas = document.querySelectorAll('div.zona');
    for (i=0;i<zonas.length;i++){
        for (node of zonas[i].childNodes) {
            node.style.background = '#ffffff';
        }
    }
}
function entra_basurero(e){
    e.preventDefault();
}
function suelta_basurero(e){
    // remover de la zona
    zona = document.getElementById('zona_' + seleccionado.id.split('_')[0]);
    for (node of zona.childNodes) {
        if (node.id == seleccionado.id){
            zona.removeChild(node);
            break;
        }
    }
}
function va_derecha(){
    if (seleccionado != null){
        // encuentra la zona
        zona = encuentra_zona(seleccionado);
        nodes = [];
        for (node of zona.childNodes){
            nodes.push(node);
        };
        // busca seleccionado en la zona
        // cloneNode clona un div
        for (i=0;i<nodes.length;i++){
            if (nodes[i].id == seleccionado.id){
                if (i<=nodes.length-2){
                    cuadroi = nodes[i].cloneNode(nodes[i],true);
                    cuadroim1 = nodes[i+1].cloneNode(nodes[i+1],true);
                    deltaim1 = parseInt(cuadroim1.style.left) - parseInt(cuadroi.style.left) - parseInt(cuadroi.style.width);
                    var temp = cuadroi;
                    nodes[i] = nodes[i+1];
                    nodes[i+1] = temp;
                    nodes[i].style.left = parseInt(cuadroi.style.left) + 'px';
                    nodes[i+1].style.left = parseInt(cuadroi.style.left) + parseInt(cuadroim1.style.width) + parseInt(deltaim1) + 'px';
                }
                break;
            };
        };
        zona.innerHTML = '';
        // outerHTML convierte un div en string
        for (i=0;i<nodes.length;i++){
            zona.innerHTML += nodes[i].outerHTML;
        };
    }
}
function hacia_izquierda(){
    if (seleccionado != null){
        // encuentra la zona
        zona = encuentra_zona(seleccionado);
        nodes = [];
        for (node of zona.childNodes){
            nodes.push(node);
        };
        // buscar el seleccionado en la zona
        for (i=0;i<nodes.length;i++){
            if (nodes[i].id == seleccionado.id){
                if (i>0){
                    cuadroi = nodes[i].cloneNode(nodes[i],true);
                    cuadroim1 = nodes[i-1].cloneNode(nodes[i-1],true);
                    deltai = parseInt(cuadroi.style.left) - parseInt(cuadroim1.style.left) - parseInt(cuadroim1.style.width);
                    nodes[i] = nodes[i-1];
                    nodes[i-1] = cuadroi;
                    nodes[i-1].style.left = parseInt(cuadroim1.style.left) + 'px';
                    nodes[i].style.left = parseInt(cuadroim1.style.left) + parseInt(cuadroi.style.width) + parseInt(deltai) + 'px';
                }
            }
       };
       zona.innerHTML = '';
       // outerHTML convierte un div en string
       for (i=0;i<nodes.length;i++){
           zona.innerHTML += nodes[i].outerHTML;
       };
}
}
function aumenta_margen(){
    if (seleccionado != null){
        // encuentra zona
        zona = encuentra_zona(seleccionado);
        for (node of zona.childNodes){
            if (node.id == seleccionado.id){
                node.style.left = parseInt(node.style.left) + parseInt(10) + 'px';
            };
        }
    };
}
function reduce_margen(){
    if (seleccionado != null){
        // encuentra zona
        zona = encuentra_zona(seleccionado);
        for (node of zona.childNodes){
            if (node.id == seleccionado.id){
                node.style.left = parseInt(node.style.left) - parseInt(10) + 'px';
            };
        }
    };
}
// Funcion que recorre todos los cuadrso desde el seleccionado hacia la derecha
function cambia_margen_izquierdo_todos(){
    if (seleccionado != null){
        // encuentra zona
        zona = encuentra_zona(seleccionado);
        var desde = false;
        for (node of zona.childNodes){
            if (node.id == seleccionado.id){
                desde = true;
            };
            if (desde == true){
                node.style.left = parseInt(node.style.left) + parseInt(10) + 'px';
            }
        }
    }
}

function encuentra_zona(elemento){
    zona = document.getElementById('zona_' + elemento.id.split('_')[0]);
    return zona;
}
function enviar(){
    // construye desde las zonas
    var arreglo = new Array();

    zonas = document.querySelectorAll('div.zona');
    for (zona of zonas){
        // define datos para calcular deltas
        left = 0;
        ancho = 0;
        for (node of zona.childNodes){
            var obj = new Object;
            obj.zonaid = node.id.split('_')[0];
            obj.propid = node.id.split('_')[1];
            obj.width = parseInt(node.style.width);
            obj.left = parseInt(node.style.left);
            obj.nombre = node.innerHTML;
            obj.delta = obj.left - left - ancho;
            console.log(obj.delta);
            left = parseInt(node.style.left);
            ancho = parseInt(node.style.width);
            arreglo.push(obj);
        };
    };
    json_envio = new Object();
    json_envio.propiedades = arreglo;
    // console.log(id_modelo);
    window.location.href = 'http://127.0.0.1:8000/modelos/reporte_lista/?criterio=&json=' + JSON.stringify(json_envio) + '&nuevo=' + nuevo + '&proyecto_id=' + id_proyecto + '&modelo_id=' + id_modelo;
}
