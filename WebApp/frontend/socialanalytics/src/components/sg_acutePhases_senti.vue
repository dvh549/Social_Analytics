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
                        <img src="../assets/negative_wordcloud_acutePhases.png" height="300px" style="margin:0 auto; display: block;">
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
                        <img src="../assets/neutral_wordcloud_acutePhases.png" height="300px" style="margin:0 auto; display: block;">

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
                        <img src="../assets/positive_wordcloud_acutePhases.png" height="300px" style="margin:0 auto; display: block;">

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
                            Positive tweets are the highest in proportion at 44%, followed by negative tweets at 32%, and then neutral tweets at 24%. This indicated that Singaporeans are happier knowing that safety measures are being further relaxed. Examples included “Singapore to simplify COVID-19 rules; safe distancing no longer required when wearing masks” and “Conquered Covid and out to celebrate!”. However, there are those that are still affected by the (possible) effects of the virus infection, and certain implemented measures. Examples included “From covid to HFMD to stomach flu to head lice. Macam2.” and “ok this covid actually annoying eh cannot go out all knn”. 
                            <strong>*Word Cloud</strong>
                            <br/>                 
                            The Omicron variant was also a worry for the community as seen in the word cloud above   
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
            bar_start:[{"name":'Sentiment',"data":[32,26,42]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [15,18,18,21,19,12,8,9,16,26,20,24,26,19,19,25,29,16,10,8,21,11,10,12,7,12,9,10,4,9,16,11,17,15,23,9,12,7,14,9,9,7,7,12,20,20,7,12,10,10,5,15,7,13,7,6,12,7,4,3,7,1]
                },
                {
                    "name":"Neutral",
                    "data": [11,11,5,18,14,25,5,11,9,20,20,18,14,17,18,38,12,5,2,5,9,5,8,5,5,2,1,7,3,4,7,6,6,6,9,4,2,6,10,3,5,1,9,6,8,7,6,6,10,9,3,8,8,0,5,7,2,2,4,3,4]
                },
                {
                    "name":"Negative",
                    "data": [10,7,15,16,19,7,11,13,10,19,16,19,19,15,12,9,19,14,7,13,14,14,9,8,5,6,6,8,9,6,19,6,9,13,11,6,8,3,8,7,4,3,5,12,15,14,6,10,5,7,2,16,9,6,10,11,6,7,9,3,3]
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
                    categories: ["2021-12-06","2021-12-13","2021-12-20","2021-12-27","2022-01-03","2022-01-10","2022-01-17","2022-01-24","2022-01-31","2022-02-07","2022-02-14","2022-02-21","2022-02-28","2022-03-07","2022-03-14","2022-03-21","2022-03-28","2022-04-04","2022-04-11","2022-04-18","2022-04-25","2022-05-02","2022-05-09","2022-05-16","2022-05-23","2022-05-30","2022-06-06","2022-06-13","2022-06-20","2022-06-27","2022-07-04","2022-07-11","2022-07-18","2022-07-25","2022-08-01","2022-08-08","2022-08-15","2022-08-22","2022-08-29","2022-09-05","2022-09-12","2022-09-19","2022-09-26","2022-10-03","2022-10-10","2022-10-17","2022-10-24","2022-10-31","2022-11-07","2022-11-14","2022-11-21","2022-11-28","2022-12-05","2022-12-12","2022-12-19","2022-12-26","2023-01-02","2023-01-09","2023-01-16","2023-01-23","2023-01-30","2023-02-06"],
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
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisAcutePhase")
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

