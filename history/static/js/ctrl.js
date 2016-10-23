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
});