<template>
<!-- Area Chart -->
    <div class="row">
        
        <div class="col-xl-12 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Analysis</h6>
                </div>
                <div class="card-body" style="height:700px; overflow-y: scroll;">
                    <div class="chart-area">
                        <p>
                            <strong>Do take note this is an analysis of quote/reply network, due to the network complexity the network is not shown </strong>
                            <br/>
                            
                            “atrupar” - an independent journalist who mainly covers US politics and media, has a high betweenness centrality. This user has been extremely active in quoting a wide variety of tweets, from news sources to government officials and adding his own opinions on that topic. His wide variety of quoting content has led to him being a connector to different groups of people. For instance, he tweets about politics and then basketball, his tweets are not bound to a certain category, as an independent journalist he brings his personal touch/life/hobbies into his tweets content too. Additionally, his style of tweeting, quoting contents, shows his dedication to be saying “my opinions are on things that are happening, not fake news”. This adding of context and substantiating with evidence helped build up his credibility leading to his large 800k Twitter followers despite being an independent journalist. The sentiment towards the topics discussed were mostly positive except for when it came to tweets about the measures implemented by Donald Trump. Despite our models predicted many “Fake News” for his tweets, our manual analysis concludes that the model predicts as such due to many of the tweets are his opinions and not a factual statement intention. 
                            <br/>
                            <br/>

                            “gtconway3d” - a former Republican now turned columnist for Washington post on politics and media, is another who has high betweenness centrality. He enters the limelight in giving opinions during news channel reporting/discussions. As a columnist, he must often share interesting news thus he quotes various contents and share his opinions to get people engaged in them. The sentiment towards the topics discussed were mostly negative. As the user is a rather prominent columnist in Washington Post, he can be a good facilitator of information given credibility is his work lifeline. As a rather famous person with 2.1million followers, he can be useful in delivering information whilst acting as a second opinion. 
                            <br/>
                            <br/>

                            “CNN” - a news media international company has high closeness and in-degree centrality. Being a news media company, it is expected of them to have a wide range of topics which interests the public. Moreover, as a news company, unbiases and impartiality is their core thus people have trust in their information resulting in quoting CNN. The sentiment towards the topics discussed had a balance of positive, neutral, and negative reactions. CNN as an established news company, is extremely useful to transmit information to majority of people given their wide audience reach. For instance, in Singapore, when masks were not mandatory, many citizens rely on CNN to receive/watch the news reporting. 
                            <br/>
                            <br/>

                            “Dsquared75” - a democrat disability and health advocate, has a high out-degree centrality. He oftens quote on content which relates to new public policies on disabilities and health. Having a high out-degree also shows that the mainly use twitter as a form of broadcasting tool to spread awareness of certain topics along with his views/opinions. The sentiment towards the topics discussed were between positive and negative reactions. Our Fake News model classifies his tweets as mainly “Fake”, however in our manual analysis, we realise that many of his tweets may be bias, not “Fake”. As a strong and vocal advocate in certain controversial topics, it is unavoidable for him to be bias. However, from the viewpoint of information spreader, he may be a strong voice if the information topic is of his talking interest (he will spread his views on them). 
                            <br/>
                            <br/>

                            “Heerak4Congress” - a republican candidate running for congress for Virginia state district. As a potential government candidate, his tweets mainly focused on his life, such as him going to Disneyland, church, and on government policies. There is not much to the user except acknowledging his relentless approach in hopes for getting noticed for congress. The sentiment towards the topics discussed were mostly negative reactions. Our model predicted mainly “Fake” news however his tweets were mainly his opinions on the quote he’s quoting. As a information broker, this user will be a poor conductor of transfer means given his lack of Followers and tweet public engagements. 
                            <br/>
                            <br/>

                            “MayorBowser” - mayor of Washington DC, who mainly focus on tweeting on progress/updates for the Washington dc. She has high closeness centrality as Washington DC citizens would often quote her tweets to share with their circle on incoming changes to their living community. It is interesting to note that despite having lesser followers than news company such as “thehill” or “CNN”, she still had a higher closeness centrality score. This means that information from this account can potentially reach a wider audience than an average news company. The sentiment towards the topics discussed were mostly positive. The Fake News model predicts half of tweets to be “Fake” news, however upon examination of the tweets, they are mainly updates of what changes are going on within the Washington DC. Also, as the official account for the mayor of Washington DC, this account is extremely important and useful in transmitting of important information to the residents of Washington dc. 
                            <br/>
                            <br/>

                            “realDonaldTrump” - 45th president of the USA personal account. He has an extremely high closeness and in-degree centrality, which is no surprise given his famous/infamous for his controversial tweets. Many people keep close check on his new tweets for different reasons (fun,laugh,idk). There is no other president who is so vocal (personal thoughts) in his tweets thus people also quote his tweets for many reasons. Additionally, he was president during the beginning of COVID thus coupled with his character, many interested parties/organisations would keep a close watch on the president views as it will greatly impact them. The sentiment towards the topics discussed had a balance of positive and negative reactions. Many of Donald trump tweets were self-opinions rather than factual news thus many of his tweets were classified “Fake” news in our model. However, as the president then, he was extremely useful in spreading information as many citizens, even before his administration were following his twitter.  
                            <br/>
                            <br/>

                            “thehill” - political news company focusing on USA, they have a high closeness and in-degree centrality. As one of the biggest and main sources of political news outlet, people during COVID wanted to be constantly updated on what the government would do next. (payout, tax rebate, mask mandates) For businesses and anxious citizens, many would quote “thehill” for latest news update which would affect their lives. The sentiment towards the topics discussed were mostly negative. As one of the main news companies focusing on Washington dc policy and political news, they rely on their trustworthiness to provide latest content to viewers. Thus, this account is extremely useful to spread latest information regarding government movements. 
                            <br/>
                            <br/>

                            “washingtonpost” - a news company, has high closeness and in-degree centrality as it is another huge news company. People who want the latest news would check to their tweets, and as supposedly trustworthy sources, people would quote them to spread awareness of certain information. The sentiment towards the topics discussed had a balance of positive and negative reactions. As a news company focusing on all topics/industry, they have a wider reach to various audiences thus to spread information, they will be ideal to help be loudspeaker to majority of the public. 
                            </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Covid")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Betweenness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in betweeness" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Covid")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Closeness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in closeness" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Covid")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>In Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in indegree" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Covid")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Out Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in outdegree" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        
    </div>

    <div class="row">
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Coronavirus")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Betweenness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in betweeness2" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Coronavirus")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Closeness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in closeness2" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Coronavirus")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>In Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in indegree2" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Coronavirus")</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Out Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in outdegree2" :key="name">
                                <td>{{name}}</td>
                                <td>{{val}}</td>
                            </tr>
                        </table>

                    </div>
                </div>
            </div>
        </div>
        
    </div>
    



</template>

<script>
import 'vis-network/styles/vis-network.css'
// import { Network } from "vis-network/peer/esm/vis-network";
// import { DataSet } from "vis-data/peer/esm/vis-data"
// import jsonData from "../assets/nodeJsonCovidReplySG.json"
// import {CovidNode} from '../config.js'
export default {
    props: {
        // positiveWordsComponent: Array,
        // negativeWordsComponent: Array,
        // neutralWordsComponent: Array
       
    },
    components: {
        // SocialNetwork
        // Network
    },
    data(){
        return{
        network:null,
        // edges: 
        betweeness:{'NickyFrank30': "3.579956336968327e-06",
                    'JoeBorelliNYC': "1.6150178963766888e-06",
                    'AirlineFlyer': "1.535612849804835e-06",
                    'ShabazzStuart': "1.4858164646665536e-06",
                    'chayesmatthew': "1.308164496065118e-06",
                    'VinPickles': "1.2476013249509921e-06",
                    'nyillini311': "1.1830006090959245e-06",
                    'ginavergel7': "1.0699493563495563e-06",
                    'Mezikenyc': "8.869139947601983e-07",
                    'Biedersam': "7.92704617471558e-07",
                    },
        closeness:{'realDonaldTrump': 0.009047335688374913,
                    'NYGovCuomo': 0.004292468665811092,
                    'Jim_Jordan': 0.0020962932294969422,
                    'JoeBiden': 0.0020934580788177044,
                    'NYCMayor': 0.0019083061931295543,
                    'thehill': 0.0019076268388422172,
                    'GOP': 0.0016938653994305337,
                    'DrEricDing': 0.0016656144786905927,
                    'ProjectLincoln': 0.0014341326995052626,
                    'SpeakerMcCarthy': 0.001251156064341859,
                    },
        indegree:{'realDonaldTrump': 0.009097912616016729,
                    'NYGovCuomo': 0.004292160387394989,
                    'Jim_Jordan': 0.0020910524964232,
                    'JoeBiden': 0.0020910524964232,
                    'thehill': 0.0019076268388422172,
                    'NYCMayor': 0.0019076268388422172,
                    'GOP': 0.0016875160497450384,
                    'ProjectLincoln': 0.001430720129131663,
                    'nypost': 0.0012472944715506804,
                    'SpeakerMcCarthy': 0.0012472944715506804,
                },
        outdegree:{'IsabelM64995699': 0.007667192486885065,
                    'MisterPatrick1': 0.0060897318316886166,
                    'NickyFrank30': 0.00605304670017242,
                    'ariccio': 0.005466084595913277,
                    'agordonstudio': 0.0050258630177189186,
                    'FanaticalModera': 0.004402215781943579,
                    'watergatesummer': 0.004328845518911185,
                    'Helen_Highly': 0.004108734729814006,
                    'jamieob256': 0.0039253090722330235,
                    'CFCCovid': 0.0033016618364576835,
                    },
        betweeness2:{'aeidinger': "8.588478629534011e-07",
                    'DougSloan': "8.195862463612456e-07",
                    'mattyglesias': "6.527243758445848e-07",
                    'samerfarha': "5.447549302161572e-07",
                    'DCHomos': "4.5150859080978803e-07",
                    'Aly_Dar8': "3.38631443107341e-07",
                    'conorjrogers': "3.239083368852827e-07",
                    'RyanLEllis': "3.190006348112633e-07",
                    'CorieWhalen': "2.7483131614508837e-07",
                    'gerald_joseph90': "2.6992361407106893e-07",
                    },
        closeness2:{'realDonaldTrump': 0.009799189883209953,
                    'thehill': 0.002171628721541156,
                    'Jim_Jordan': 0.002031523642732049,
                    'GOP': 0.001681260945709282,
                    'CNN': 0.0016682279151223882,
                    'SpeakerMcCarthy': 0.0015411558669001751,
                    'washingtonpost': 0.0014010507880910684,
                    'MollyJongFast': 0.0013343340838962556,
                    'MarshaBlackburn': 0.0013309982486865149,
                    'atrupar': 0.0013309982486865149,
                    },
        indegree2:{'realDonaldTrump': 0.010017513134851138,
                    'thehill': 0.002171628721541156,
                    'Jim_Jordan': 0.002031523642732049,
                    'CNN': 0.0017513134851138354,
                    'GOP': 0.001681260945709282,
                    'SpeakerMcCarthy': 0.0015411558669001751,
                    'washingtonpost': 0.0014010507880910681,
                    'MarshaBlackburn': 0.0013309982486865149,
                    'atrupar': 0.0013309982486865149,
                    'kylegriffin1': 0.0013309982486865149,
                },
        outdegree2:{'HajjiADavis': 0.013099824868651489,
                    'diasporaonline': 0.011418563922942207,
                    'fabucat': 0.010367775831873906,
                    'koamac': 0.006024518388791593,
                    'NotoriousRBF': 0.005253940455341506,
                    'VincentDiazJr1': 0.005253940455341506,
                    'Lee4Pete': 0.005183887915936953,
                    'tomsommers1': 0.005183887915936953,
                    'freelancerjourn': 0.004903677758318739,
                    'Aly_Dar8': 0.004903677758318739,
                    },



        betweeness3:{'SquarePegDem': "3.654374647918877e-06",
                    'bobhardt': "2.1449590324741236e-06",
                    'RobGeorge': "1.3108082976230755e-06",
                    'MarkLevineNYC': "1.0327580526727262e-06",
                    'ClaudeBrodesser': "9.533151255440549e-07",
                    'AnnieTangent': "3.17771708514685e-07",
                    'alextarquinio': "1.588858542573425e-07",
                    'RMillennielle': "7.944292712867125e-08",
                    'JoeBorelliNYC': "3.972146356433562e-08",
                    'CarriageCavalry': "3.972146356433562e-08",
                    },
        closeness3:{'realDonaldTrump': 0.025508170585890794,
                    'NYGovCuomo': 0.008374397623102285,
                    'thehill': 0.00438421681944998,
                    'WhiteHouse45': 0.0035870864886408927,
                    'CNN': 0.0035870864886408927,
                    'JoeBiden': 0.0025906735751295338,
                    'nytimes': 0.0025906735751295338,
                    'chrislhayes': 0.0019928258270227183,
                    'nypost': 0.0019811033221578786,
                    'atrupar': 0.0017935432443204463
                    },
        indegree3:{'realDonaldTrump': 0.025508170585890794,
                    'NYGovCuomo': 0.008369868473495417,
                    'thehill': 0.00438421681944998,
                    'WhiteHouse45': 0.003587086488640893,
                    'CNN': 0.003587086488640893,
                    'JoeBiden': 0.0025906735751295338,
                    'nytimes': 0.0025906735751295338,
                    'nypost': 0.0019928258270227183,
                    'chrislhayes': 0.0019928258270227183,
                    'atrupar': 0.0017935432443204466,
                },
        outdegree3:{'Israelmarrero10': 0.01733758469509765,
                    'KevinClamato': 0.016739736946990835,
                    'RonWaxman': 0.014348345954563572,
                    'Helen_Highly': 0.01195695496213631,
                    'Lindasantangel1': 0.010163411717815863,
                    'lu_lu52': 0.00996412913511359,
                    'Lauryn2000': 0.00876843363889996,
                    'RMontea4': 0.0073734555599840575,
                    'IsraelRoseMarr1': 0.0073734555599840575,
                    'bjorn6': 0.007174172977281786,
                    },
        

        
        betweeness4:{'atrupar': 1.0232513402034428e-06,
                    'nathanking': 6.821675601356286e-07,
                    'DMVBlackLives': 5.116256701017214e-07,
                    'MrTinDC': 3.410837800678143e-07,
                    'HollyLiveFox5DC': 1.7054189003390714e-07,
                    'BlakeMcCoyTV': 1.7054189003390714e-07,
                    'kikilitalien': 1.7054189003390714e-07,
                    'jimfusillibooks': 0.0,
                    'MarshaBlackburn': 0.0,
                    'cactusapinyona': 0.0,
                    },
        closeness4:{'realDonaldTrump': 0.026424442609413706,
                    'WhiteHouse45': 0.0053674649050371595,
                    'kylegriffin1': 0.0037159372419488025,
                    'Mike_Pence': 0.0037159372419488025,
                    'GOP': 0.0033030553261767133,
                    'SpeakerMcCarthy': 0.002890173410404624,
                    'thehill': 0.002890173410404624,
                    'MSNBC': 0.002890173410404624,
                    'washingtonpost': 0.002890173410404624,
                    'CNN': 0.002477291494632535,

                    },
        indegree4:{'realDonaldTrump': 0.026424442609413706,
                    'WhiteHouse45': 0.005367464905037159,
                    'kylegriffin1': 0.0037159372419488025,
                    'Mike_Pence': 0.0037159372419488025,
                    'GOP': 0.0033030553261767133,
                    'SpeakerMcCarthy': 0.002890173410404624,
                    'thehill': 0.002890173410404624,
                    'MSNBC': 0.002890173410404624,
                    'washingtonpost': 0.002890173410404624,
                    'CNN': 0.002477291494632535,
                },
        outdegree4:{'HajjiADavis': 0.02972749793559042,
                    'freelancerjourn': 0.016515276630883566,
                    'Hoosier84': 0.012799339388934764,
                    'fabucat': 0.010734929810074317,
                    'twright55': 0.010322047894302229,
                    'VincentDiazJr1': 0.00990916597853014,
                    'orecule': 0.009496284062758051,
                    'Steadyruncho123': 0.007844756399669695,
                    'francvs': 0.007431874483897605,
                    'Chris_nDC': 0.007018992568125515
                    },



        }
  }, 
    mounted() {
        // const container = this.$refs.graph
        // var nodes = new DataSet(jsonData.nodes)
        // var edges = new DataSet(jsonData.edges)

        // const data = {
        // nodes: nodes,
        // edges: edges
        // }
        // const options = {
        //      interaction: {
        //         navigationButtons: true,
        //         zoomView: true, // Enable zooming
        //         dragView: true, // Enable panning 
        //     },
        //     layout:{
        //         improvedLayout:false
        //     },
        //      nodes: {
        //         size: 10
        //     }
            

        // }
        // console.log("HERE")
        // // new Network(container, data, options)
        // var network = new Network(container, data, options)
        // this.network= network
        // this.zoomToNode(2);
            
        

    },
    methods: {
        //  zoomToNode(nodeId) {
            
        //         var position = this.network.getPositions()[nodeId];
        //         this.network.focus(2,{
        //             position: {x:position.x, y:position.x},
        //             offset: position,
        //             scale: 1,
        //             locked: false,
        //         });
           
        // },
        
    }


}
</script>

<style scoped>
    table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
    
    }
</style>
