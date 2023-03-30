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
                        <img src="../assets/negative_wordcloud_green_us.png" height="300px" style="margin:0 auto; display: block;">
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
                        <img src="../assets/neutral_wordcloud_green_us.png" height="300px" style="margin:0 auto; display: block;">

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
                        <img src="../assets/positive_wordcloud_green_us.png" height="300px" style="margin:0 auto; display: block;">

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
                            Positive tweets are the highest in proportion at 44%, followed by negative tweets at 40% (in close second), and neutral tweets at 16%. The community was concerned and doubtful about government measures by sharing tweets like “En Us Covid Commission Slams Governments Response As Untrustworthy Urges Investigation Into Virus Origins” to discuss Government’s responses with to Covid with a <a href="https://www.msn.com/en-us/health/other/covid-19-commission-slams-governments-response-as-untrustworthy-urges-investigation-into-virus-origins/ar-AA11QA9l">link</a> to an article detailing the event. <br/>
                            <strong>*Line Chart</strong>
                            <br/>
                            Most notably, it was at point a) that negative tweets peaked the most. It may be likely due to the community’s concerns about long covid with them sharing tweets such as “New research finds that serious cases of COVID-19 could lead to an increased risk of Long COVID symptoms.”. 
                            <br/>
                            <strong>*Conclude</strong>
                            <br/>
                            Preventative measures were generally well received by the community except for the years 2021 and 2022 where people were concerned about the side effects of contracting covid-19 and its vaccines 
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
            bar_start:[{"name":'Sentiment',"data":[39,17,43]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [88,210,122,102,79,72,54,56,41,54,60,64,38,65,71,42,82,63,45,83,64,60,62,70,77,54,58,55,74,112,91,60,37,74,60,43,53,56,67,77,44,75,81,51,43,40,34,35,43,54,52,41,37]
                },
                {
                    "name":"Neutral",
                    "data": [36,100,52,60,29,27,33,13,21,22,18,38,16,29,19,23,24,27,21,22,26,18,31,32,32,20,20,31,21,44,40,21,18,18,18,20,28,23,25,16,21,20,22,22,10,14,15,15,17,29,22,15,16]
                },
                {
                    "name":"Negative",
                    "data": [80,209,135,104,77,70,51,37,37,36,33,46,29,47,45,43,63,39,43,51,59,44,54,63,55,39,54,41,72,85,75,52,38,63,44,41,54,58,81,76,62,83,65,54,56,54,47,35,33,57,50,47,37]
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
                    categories: ["2022-01-03","2022-01-10","2022-01-17","2022-01-24","2022-01-31","2022-02-07","2022-02-14","2022-02-21","2022-02-28","2022-03-07","2022-03-14","2022-03-21","2022-03-28","2022-04-04","2022-04-11","2022-04-18","2022-04-25","2022-05-02","2022-05-09","2022-05-16","2022-05-23","2022-05-30","2022-06-06","2022-06-13","2022-06-20","2022-06-27","2022-07-04","2022-07-11","2022-07-18","2022-07-25","2022-08-01","2022-08-08","2022-08-15","2022-08-22","2022-08-29","2022-09-05","2022-09-12","2022-09-19","2022-09-26","2022-10-03","2022-10-10","2022-10-17","2022-10-24","2022-10-31","2022-11-07","2022-11-14","2022-11-21","2022-11-28","2022-12-05","2022-12-12","2022-12-19","2022-12-26","2023-01-02"],
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
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisGreenUS")
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

