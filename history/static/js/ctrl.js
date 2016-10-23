angular.module('myApp', ['angularMoment'])
.controller('CtrlIndex', function ($scope, $http) {
    startTime();
    function startTime(){
        $http({
            method: 'GET',
            url: '/api/dashboard/'
        }).
        then(function successCallback(response) {
            $scope.retorno = response.data;
            
            for(var i = 0; i < response.data.desks.length; i++){
                response.data.desks[i].start = diferenciarDatas(response.data.desks[i].start);
                if(response.data.desks[i].finish != null){
                    response.data.desks[i].finish = diferenciarDatas(response.data.desks[i].finish);
                }
            }
            $scope.orders = response.data.desks;
        });
        var t = setTimeout(function(){ startTime() }, 200);
    }
	

    function diferenciarDatas(data){
        var velho = moment(data); //data do obj recebido
        var novo = moment(); // data do obj atual
        var result = novo.diff(velho); // resultado da diferença de datas em milisegundos
        return moment().millisecond(result).format('h:mm:ss'); // formatação da data
    }
})


.controller('CtrlResultados', function ($scope, $http) {
    $http({
        method: 'GET',
        url: '/api/history/order/1/productivity/'
    }).
    then(function successCallback(response) { 
        result= response.data;
        new Chart(document.getElementById("line_chart").getContext("2d"), getChartJs('line'));
    });

    //Criar as labels do gráfico
    function dividirDias(prazo){
        var dias = [];
        for (var i = 0; i < prazo; i++) {
            dias[i] = "Dia "+(i+1);
        }
        return dias;
    }

    //calcula o mínimo que pode ser feito por dia, para que seja entregue no prazo correto
    function calcularProducaoMedia(prazo, total) {
        var prod = [];
        var prodDia = total/prazo;
        for (var i = 0; i < prazo; i++) {
            if(i == 0){
                prod[i] = prodDia;
            } else{
                prod[i] = prod[i-1] + prodDia;
            }
        }
        return prod;
    }

    // Gera o gráfico
    function getChartJs(type) {
        var config = null;
        config = {
            type: 'line',
            data: {
                labels: dividirDias(result.deadline),
                datasets: [{
                    label: "Resultado Esperado",
                    data: result.histories,
                    borderColor: 'rgba(0, 188, 212, 0.75)',
                    backgroundColor: 'rgba(0, 188, 212, 0.3)',
                    pointBorderColor: 'rgba(0, 188, 212, 0)',
                    pointBackgroundColor: 'rgba(0, 188, 212, 0.9)',
                    pointBorderWidth: 1
                }, /*{
                    label: "Resultado Alcançado",
                    data: result.histories,
                    borderColor: 'rgba(233, 30, 99, 0.75)',
                    backgroundColor: 'rgba(233, 30, 99, 0.3)',
                    pointBorderColor: 'rgba(233, 30, 99, 0)',
                    pointBackgroundColor: 'rgba(233, 30, 99, 0.9)',
                    pointBorderWidth: 1
                    },*/
                    {
                    label: "Resultado Médio",
                    data: calcularProducaoMedia(result.deadline, result.quantity),
                    borderColor: 'rgba(50, 50, 50, 0.75)',
                    backgroundColor: 'rgba(50, 50, 50, 0.3)',
                    pointBorderColor: 'rgba(50, 50, 50, 0)',
                    pointBackgroundColor: 'rgba(50, 50, 50, 0.9)',
                    pointBorderWidth: 1
                    }]
            },
            options: {
                responsive: true,
                legend: false
            }
        }
        return config;
    }
});