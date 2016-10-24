angular.module('myApp', ['angularMoment'])
.controller('CtrlIndex', function ($scope, $http) {
    startTime();
    function startTime(){
        $http({
            method: 'GET',
            url: '/history/api/dashboard/'
        }).
        then(function successCallback(response) {
            $scope.retorno = response.data;
            
            for(var i = 0; i < response.data.desks.length; i++){
                response.data.desks[i].start = diferenciarDatas(response.data.desks[i].start);
                if(response.data.desks[i].finish != null){
                    response.data.desks[i].finish = diferenciarDatas(response.data.desks[i].finish);
                }
            }
            $scope.desks = response.data.desks;
        });
        var t = setTimeout(function(){ startTime() }, 200);
    }
	

    function diferenciarDatas(data){
        var velho = moment(data); //data do obj recebido
        var novo = moment(); // data do obj atual
        var result = novo.diff(velho); // resultado da diferença de datas em milisegundos
        return moment().millisecond(result).format('hh:mm:ss'); // formatação da data
    }
})

.controller('CtrlResultados', function ($scope, $http) {
    $http({
        method: 'GET',
        url: 'http://smartwork-web.herokuapp.com/history/api/order/1/productivity/'
    }).
    then(function successCallback(response) {
        result= response.data;
        $scope.diasRestantes = result.deadline - result.histories.length;
        $scope.totalProduzido = result.histories[result.histories.length-1];
        $scope.restante = result.quantity - $scope.totalProduzido;
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
    function calcularProducaoMedia(prazo, total, historico) {
        var prod = [];
        for (var i = 0; i < historico.length; i++) {
            restante = total - historico[i];
            if(restante > 0){
                prod[i+1] =  restante/(prazo-i);
            }
        }
        return prod;
    }

    // retorna o valor diário produzido
    function parser(historico) {
        for (var i = 0; i < historico.length; i++) {
            if(i != 0)
                historico[i] = historico[i] - historico[i-1] ;
        }
        return historico;
    }

    // Gera o gráfico
    function getChartJs(type) {
        var config = null;
        config = {
            type: 'line',
            data: {
                labels: dividirDias(result.deadline),
                datasets: [{
                    label: "Resultado Produzido",
                    data: parser(result.histories),
                    borderColor: 'rgba(0, 188, 212, 0.75)',
                    backgroundColor: 'rgba(0, 188, 212, 0.3)',
                    pointBorderColor: 'rgba(0, 188, 212, 0)',
                    pointBackgroundColor: 'rgba(0, 188, 212, 0.9)',
                    pointBorderWidth: 1
                }, {
                    label: "Resultado Médio",
                    data: calcularProducaoMedia(result.deadline, result.quantity, result.histories),
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