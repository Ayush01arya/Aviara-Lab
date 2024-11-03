angular.module('myApp', [])
.controller('MainController', function($scope, $http) {
    var vm = this;
    vm.pdfFiles = [];
    vm.isTraining = false;
    vm.progress = 0;
    vm.trainingCompleted = false;
    vm.question = '';
    vm.response = '';
    vm.modalVisible = false;

    vm.openModal = function() {
        vm.modalVisible = true;
    };

    vm.closeModal = function() {
        vm.modalVisible = false;
        vm.resetForm();
    };

    vm.resetForm = function() {
        vm.pdfFiles = [];
        vm.isTraining = false;
        vm.progress = 0;
        vm.trainingCompleted = false;
        vm.question = '';
        vm.response = '';
    };

    vm.handleFileSelect = function() {
        var fileInput = document.getElementById('pdfFiles');
        vm.pdfFiles = Array.from(fileInput.files);

        if (vm.pdfFiles.length === 0) {
            alert("Please select at least one PDF file.");
        }
    };

    vm.trainPDF = function() {
        if (vm.pdfFiles.length === 0) {
            alert("Please select at least one PDF file.");
            return;
        }

        vm.isTraining = true;
        vm.progress = 0;

        // Simulating training process
        var interval = setInterval(function() {
            if (vm.progress < 100) {
                vm.progress += 10;
                $scope.$apply(); // Update scope for AngularJS
            } else {
                clearInterval(interval);
                vm.isTraining = false;
                vm.trainingCompleted = true;
            }
        }, 1000);
    };

    vm.handleQuestion = function() {
        if (!vm.question) {
            vm.response = "Please enter a question.";
            return;
        }

        // Here, you would make a call to your backend API
        $http.post('http://127.0.0.1:5000/ask-question', { question: vm.question })
            .then(function(response) {
                vm.response = response.data.reply || "No reply available.";
            })
            .catch(function(error) {
                console.error("Error asking question:", error);
                vm.response = "Error fetching answer. Please try again.";
            });
    };
});
