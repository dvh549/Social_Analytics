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
                        <img src="../assets/negative_wordcloud_green.png" height="300px" style="margin:0 auto; display: block;">
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
                        <img src="../assets/neutral_wordcloud_green.png" height="300px" style="margin:0 auto; display: block;">

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
                        <img src="../assets/positive_wordcloud_green.png" height="300px" style="margin:0 auto; display: block;">

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
                            Positive tweets are the highest in proportion at 41%, followed by negative tweets at 38%, and then neutral tweets at 21%. This indicated that Singaporeans were happier knowing that safety measures were mostly being relaxed. Face to face interactions have returned. An example is “Hosting first offline Summit after 3 years of Covid life and also Tencent’s very first move in Web3. Nice to meet the local community in Singapore.”. We also noticed how people’s attentions have shifted from health-related issues to data loss concerns because of remote work. An example is “In the wake of the COVID-19 pandemic, remote work has become more common, leading to an increased risk of data loss.”. 
                            <strong>Conclude</strong>
                            <br/>                 
                            In general, preventative measures were well-received by the community and the community was compliant when it came to getting vaccinated for protection. 
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
            bar_start:[{"name":'Sentiment',"data":[38,22,40]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [8,13,7,11,19]
                },
                {
                    "name":"Neutral",
                    "data": [2,4,3,6,16]
                },
                {
                    "name":"Negative",
                    "data": [3,9,7,8,28]
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
                    categories: ["2023-02-06","2023-02-13","2023-02-20","2023-02-27","2023-03-06"],
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
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisGreen")
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

