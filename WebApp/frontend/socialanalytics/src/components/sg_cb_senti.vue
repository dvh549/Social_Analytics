<template>
<!-- Area Chart -->
    <div class="row">
        
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Negative</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <img src="../assets/negative_wordcloud_cb.png" height="300px" style="margin:0 auto; display: block;">
                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Neutral</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <img src="../assets/neutral_wordcloud_cb.png" height="300px" style="margin:0 auto; display: block;">

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-4 col-lg-7" >
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Word Cloud Positive</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                        <!-- {{this.positiveWordsComponent}} -->
                        <img src="../assets/positive_wordcloud_cb.png" height="300px" style="margin:0 auto; display: block;">

                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row" >
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Distribution of Sentiments in Tweets</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:400px">
                    <div class="chart-area">
                         <apexchart type="bar" height="350" :options="barChartOptions" :series="bar_start"></apexchart>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row" v-if="this.lineData[0].data!=[] && lineChartOptions.xaxis.categories!=[]">

        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Sentiment of Tweets (Weekly)</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body mb-3" style="height:600px">
                    <div class="chart-area">
                       <apexchart type="line" height="500" :options="lineChartOptions" :series="lineData"></apexchart>
                    </div>
                </div>
            </div>
        </div>

    </div>
    <div class="row" >
        <div class="col-xl-12 col-lg-12">
            <div class="card shadow mb-4">
                <!-- Card Header - Dropdown -->
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Analysis</h6>
                </div>
                <!-- Card Body -->
                <div class="card-body" style="height:300px">
                    <div class="chart-area">
                        <p>
                            <strong>*Bar Graph</strong>
                            <br/>
                            Positive tweets are the highest in proportion at 50%, followed by negative tweets at 26%, and in close third, neutral tweets at 24%. This indicated that the circuit breaker measures were acknowledged by the public as good to prevent the spread of the virus. Examples include “Border enforcement measures to prevent the spread of novel coronavirus (COVID-19)” and “Circuit breaker is defined as an automatic device for stopping the flow of current in an electric circuit as a safety measure. It keeps us safe from Covid 19. Missing the sun. #covid19 #coronavirus #stayhome”. However, people were still anxious about finding jobs. An example was “Looking forward to seeing how Singapore’s 4th #COVID__19 budget addresses the critical #upskilling agenda”. 
                            <br/>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
// import wordcloud from 'vue-wordcloud'
// import VueWordCloud from 'vuewordcloud';
// import wordcloud from 'vue-wordcloud'
// import Vue3WordCloud from 'vue3-word-cloud';
// import axios from "axios";

export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        
    },
    data(){
        return{
            bar_start:[{"name":'Sentiment',"data":[30,28,42]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [142,149,128,96,90,66,70,56,57,52,42,33,37,38,45,33,41,37,38,27,31,21,30,26,27,23,33,28,18,22,18,20,28,24,15,17,20,24,25,32,28,24,17,19,12,18,12,16,12,16,11,12,17,20,18,37,31,33,56,31,36,27,18,17,11,24,28,58,31,23,25,31,13,15,25,28,19,18,30,36,29,28,12,14,25,13,24,20,18,18,21,19,12,8,9,16,26,20,24,26,19,19,25,29,16,10,8,21,11,10,12,7,12,2]
                },
                {
                    "name":"Neutral",
                    "data": [82,81,92,44,48,35,32,30,40,28,29,20,21,20,20,22,26,11,19,34,15,9,11,12,6,8,25,21,20,15,18,10,12,12,6,15,12,15,13,18,12,16,11,15,8,11,7,8,8,5,6,6,17,15,6,18,22,16,46,22,20,26,18,19,19,16,16,33,29,20,27,18,16,16,16,25,7,19,24,40,25,28,24,16,17,18,20,12,11,5,18,14,25,5,11,9,20,20,18,14,17,18,38,12,5,2,5,9,5,8,5,5,2,1]
                },
                {
                    "name":"Negative",
                    "data": [88,86,61,70,44,29,34,37,28,15,21,18,24,24,11,13,21,16,19,23,16,15,16,14,29,15,36,31,21,15,15,16,27,11,16,15,9,15,10,29,16,23,16,12,11,9,13,8,11,5,11,15,4,10,12,25,36,16,35,22,28,23,11,14,14,23,34,62,34,37,20,20,11,15,15,36,22,23,20,37,29,22,13,15,12,17,20,14,7,15,16,19,7,11,13,10,19,16,19,19,15,12,9,19,14,7,13,14,14,9,8,5,6,1]
                }
            ],
            lineChartOptions: {
                chart: {
                    type: 'line'
                    
                },
                colors: ['#00FF00', '#FFFF00', '#FF0000'],
                // dataLabels: {
                // enabled: true,
                // },
                stroke: {
                    curve: 'smooth'
                },
                
                markers: {
                size: 1
                },
                xaxis: {
                    categories: ["2020-04-06","2020-04-13","2020-04-20","2020-04-27","2020-05-04","2020-05-11","2020-05-18","2020-05-25","2020-06-01","2020-06-08","2020-06-15","2020-06-22","2020-06-29","2020-07-06","2020-07-13","2020-07-20","2020-07-27","2020-08-03","2020-08-10","2020-08-17","2020-08-24","2020-08-31","2020-09-07","2020-09-14","2020-09-21","2020-09-28","2020-10-05","2020-10-12","2020-10-19","2020-10-26","2020-11-02","2020-11-09","2020-11-16","2020-11-23","2020-11-30","2020-12-07","2020-12-14","2020-12-21","2020-12-28","2021-01-04","2021-01-11","2021-01-18","2021-01-25","2021-02-01","2021-02-08","2021-02-15","2021-02-22","2021-03-01","2021-03-08","2021-03-15","2021-03-22","2021-03-29","2021-04-05","2021-04-12","2021-04-19","2021-04-26","2021-05-03","2021-05-10","2021-05-17","2021-05-24","2021-05-31","2021-06-07","2021-06-14","2021-06-21","2021-06-28","2021-07-05","2021-07-12","2021-07-19","2021-07-26","2021-08-02","2021-08-09","2021-08-16","2021-08-23","2021-08-30","2021-09-06","2021-09-13","2021-09-20","2021-09-27","2021-10-04","2021-10-11","2021-10-18","2021-10-25","2021-11-01","2021-11-08","2021-11-15","2021-11-22","2021-11-29","2021-12-06","2021-12-13","2021-12-20","2021-12-27","2022-01-03","2022-01-10","2022-01-17","2022-01-24","2022-01-31","2022-02-07","2022-02-14","2022-02-21","2022-02-28","2022-03-07","2022-03-14","2022-03-21","2022-03-28","2022-04-04","2022-04-11","2022-04-18","2022-04-25","2022-05-02","2022-05-09","2022-05-16","2022-05-23","2022-05-30","2022-06-06"],
                    title: {
                        text: 'Date'
                    }
                },
                legend: {
                position: 'top',
                horizontalAlign: 'right',
                floating: true,
                offsetY: -25,
                offsetX: -5
                }
            },
            barChartOptions: {
                chart: {
                type: 'bar',
                },
                plotOptions: {
                bar: {
                    distributed: true,
                    horizontal: false,
                    columnWidth: '55%',
                    endingShape: 'rounded'
                },
                },
                colors: ['#00FF00', '#FFFF00', '#FF0000'],
                dataLabels: {
                enabled: false
                },
                stroke: {
                show: true,
                width: 2,
                colors: ['transparent']
                },
                xaxis: {
                categories: ['Positive',"Neutral", "Negative"],
                },
                fill: {
                opacity: 1
                }
            }  
        }
  }, 
    // async mounted(){
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisCB")
    //         .then(res=>{
    //         console.log(res.data.message)
    //         this.lineChartOptions.xaxis.categories = res.data.message.dateaxis
    //         // this.lineChartOptions.xaxis.type = 'datetime';
    //         // this.lineChartOptions.xaxis.categories = res.data.message.dateaxis.map(dateStr => new Date(dateStr).getTime());
    //         this.lineData[0].data = res.data.message.line_start.data.positive
    //         this.lineData[1].data = res.data.message.line_start.data.neutral
    //         this.lineData[2].data = res.data.message.line_start.data.negative
    //         this.bar_start[0].data =res.data.message.bar_start
    //         console.log(this.lineChartOptions.xaxis.categories)

    //         // console.log(res.data.message.wordCloud.positive)
    //         // this.positiveWords= res.data.message.wordCloud.positive
    //         // this.negativeWords= res.data.message.wordCloud.negative
    //         // this.neutralWords= res.data.message.wordCloud.neutral
    //         // console.log(this.positiveWords)
    //         // console.log(this.negativeWords)
    //         // console.log(this.neutralWords)
            

    //         })
    // }


}
</script>

