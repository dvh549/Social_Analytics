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
                        <img src="../assets/negative_wordcloud_acutePhases_us.png" height="300px" style="margin:0 auto; display: block;">
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
                        <img src="../assets/neutral_wordcloud_acutePhases_us.png" height="300px" style="margin:0 auto; display: block;">

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
                        <img src="../assets/positive_wordcloud_acutePhases_us.png" height="300px" style="margin:0 auto; display: block;">

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
                            Positive tweets are the highest in proportion at 42%, followed by negative tweets at 41% (in close second), and neutral tweets at 17%. The community had a mix of positive and negative reactions. Examples included “A year ain’t shit no more especially post covid” and “I feel like shit after getting the covid booster shot. Damn it China”, where Americans were still convinced that China was the cause of Covid. <br/>
                            <strong>*Line Chart</strong>
                            <br/>
                            The public's negative sentiment to the covid vaccine is further supported by the multiple times the frequency of negative tweets were higher than positive tweets.  
                            <br/>
                            <strong>*Word Cloud</strong>
                            <br/>
                            It was noticeable that “vaccine” frequently appeared and was likely to be a main contributor to the community's discontent. Tweets like “Pushing ineffective and unsafe existing highly experimental mRNA COVID vaccines pricks the conscience of @FDA experts who know the scientific evidence of tens of thousands of adverse reactions from which thousands have died in USA alone, as documented.” and “A lot of fully COVID-VACCINATED are getting infected with COVID-19, proving that COVID VACCINE PASSPORT MANDATE is unreasonable. We need a new, effective vaccine that can block COVID infections. Have you heard of people getting chicken pox after getting chicken pox vaccine?”. These tweets showcased how the community was voicing out their concerns about the effectiveness of the vaccines.  
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
            bar_start:[{"name":'Sentiment',"data":[40,19,41]}],
            lineData:[
                {
                    "name":"Positive",
                    "data": [122,223,215,286,278,195,141,153,233,270,249,168,146,181,158,161,127,135,123,128,135,111,88,88,90,90,78,81,108,155,180,184,164,226,169,144,164,193,156,146,100,71,117,87,111,81,78,74,86,90,224,310,161]
                },
                {
                    "name":"Neutral",
                    "data": [48,143,101,151,108,79,73,87,83,82,91,85,79,73,85,82,65,59,57,59,66,50,37,51,32,31,48,40,66,69,104,67,76,76,92,68,69,85,67,62,50,50,59,46,46,33,42,46,36,36,125,134,72]
                },
                {
                    "name":"Negative",
                    "data": [195,235,194,292,219,212,197,156,196,214,193,153,118,135,160,185,138,87,67,100,89,93,81,94,90,99,80,86,127,165,209,166,188,193,193,154,212,261,168,188,137,119,142,94,93,72,73,71,80,70,184,237,173]
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
                    categories: ["2021-01-04","2021-01-11","2021-01-18","2021-01-25","2021-02-01","2021-02-08","2021-02-15","2021-02-22","2021-03-01","2021-03-08","2021-03-15","2021-03-22","2021-03-29","2021-04-05","2021-04-12","2021-04-19","2021-04-26","2021-05-03","2021-05-10","2021-05-17","2021-05-24","2021-05-31","2021-06-07","2021-06-14","2021-06-21","2021-06-28","2021-07-05","2021-07-12","2021-07-19","2021-07-26","2021-08-02","2021-08-09","2021-08-16","2021-08-23","2021-08-30","2021-09-06","2021-09-13","2021-09-20","2021-09-27","2021-10-04","2021-10-11","2021-10-18","2021-10-25","2021-11-01","2021-11-08","2021-11-15","2021-11-22","2021-11-29","2021-12-06","2021-12-13","2021-12-20","2021-12-27","2022-01-03"],
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
    //     await axios.get("http://127.0.0.1:5000/getSentimentAnalysisAcutePhaseUS")
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

