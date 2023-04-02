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
                            <strong>Due to the network complexity, the graph cannot be shown. Only the analysis of the quote/reply network is shown.</strong>
                            <br/>
                            
                            “aeidinger” - Washington dc businessman and cannabis rights activities. His tweets have covered many different topics, cannabis, politics, more. As he has many hands in different topics, he often replies to other users tweets which is evident in his high betweenness centrality score. The sentiment towards the topics discussed was mostly negative.  
                            <br/>
                            <br/>

                            “Aly_Dar8” - a paediatric nurse and feminist, she has a considerably high out-degree and betweenness centrality. As she is very vocal in health and #prochoice #childfree, meaning she often replies to tweets on health related and politics news. Although independent, she has a high score of being able to connect with various topic groups. The sentiment towards the topics discussed had a balance of positive and negative reactions. As an independent voice, most of her tweets revolve her opinions thus as an information broker, she may not be ideal given her small followers reach.  
                            <br/>
                            <br/>

                            “atrupar” - he is an independent journalist focusing on government policies and national politics. He also have a high influence in the Quote Network, meaning he often quote many others (gov, news,..). This also ties well in the Reply Network, and it shows, as he not only quote others, he engages in conversation with others. This can be inferred as he is really motivated, interested thus willing to discuss about various topics of his interests. The sentiment towards the topics discussed was mostly negative. Being an independent journalist, he has a wide number of followers and can be a good account to pass information to others.  
                            <br/>
                            <br/>

                            “diasporaonline” - insurance and Financial Services Advisor and writer. He discusses on topics related to businesses, governments policies, police and security. However, as this user only have a high out-degree score, it can be concluded he is not influential but simply a busybody who is vocal in his thoughts, which may not be significant. The sentiment towards the topics discussed had a balance of neutral and negative reactions. As a financial advisor, he has to be trustworthy in his sources and advice, however as an information broker, he has only a small reach. 
                            <br/>
                            <br/>

                            “DougSloan” - a political analyst and democratic strategist (TV analyst). As he is a TV analyst, not one that is on TV, his influence is just like his career/hobby, only popular within his home. Thus, to increase his influences/spread his awareness, he actively replies to many in hopes of return messages. However, as this person does not have any other outstanding/prominent centrality metrics, it can be deduce that people probably find his information to be useless or maybe him. His high betweenness means he simply replies to almost everything and bridges different topics/discussions. The sentiment towards the topics discussed had a balance of positive, neutral, and negative reactions. This user has a small reach of 3k, as an independent “political analyst”, he will be a good outlet to spread information on political policies.  
                            <br/>
                            <br/>

                            “HajiADavis” - a photographer who is interested in everything from Science, History etc. He also tweets/replies to anything that catches his interest. His whimsical nature is just as flimsy as his career, trying to leave his mark and attention thru his frantic 3am tweets for people to notice his motivation to not be a nobody. The sentiment towards the topics discussed had a balance of positive and negative reactions. This user will not be a good outlet to spread information, given how small reach he has. 
                            <br/>
                            <br/>

                            “thehill” - news company focusing on political news, having a high closeness and in-degree centrality is expected as many people relies on them for latest news. In the Reply Network, it can also be seen that majority people are replying to their tweets which are not significant. The sentiment towards the topics discussed was mostly negative. As a political news focused company, this account is extremely useful in transfer of information of latest political news. 
                            <br/>
                            <br/>

                            “realDonaldTrump” - controversial as he is, people are constantly quoting and replying to his tweets to share their opinions, small/big and insignificant/significant. The sentiment towards the topics discussed had a balance of positive and negative reactions. This is undoubtedly the best account to spread information to the largest number of people, given his infamy of tweet contents and meme surrounding him.
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
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Covid" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Covid" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Covid" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Covid" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Coronavirus" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Coronavirus" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Coronavirus" New York)</h6>
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
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Coronavirus" New York)</h6>
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
    <div class="row">
        <div class="col-xl-3 col-lg-7" >
            <div class="card shadow mb-4">
                <div
                    class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Covid" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Betweenness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in betweeness3" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Covid" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Closeness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in closeness3" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Covid" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>In Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in indegree3" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Covid" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Out Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in outdegree3" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">Betweenness Centrality ("Coronavirus" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Betweenness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in betweeness4" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">Closeness Centrality ("Coronavirus" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Closeness Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in closeness4" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">In Degree Centrality ("Coronavirus" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>In Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in indegree4" :key="name">
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
                    <h6 class="m-0 font-weight-bold text-primary">Out Degree Centrality ("Coronavirus" Washington)</h6>
                </div>
                <div class="card-body" style="height:700px">
                    <div class="chart-area">
                        <table style="height:600px; width:100%">
                            <tr>
                                <th>User</th>
                                <th>Out Degree Centrality</th>
                            </tr>
                            <tr v-for="(val, name)  in outdegree4" :key="name">
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
// import jsonData from "../assets/nodeJson.json"
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
        betweeness:{'MarkLevineNYC': "3.951452063279682e-06",
                    'JoeBorelliNYC': "2.3113706084435205e-06",
                    'CarlinaRivera': "2.2732291792612844e-06",
                    'WalkerBragman': "1.0069337304110386e-06",
                    'celinegounder': "7.933417269905153e-07",
                    'ydanis': "6.407760102615701e-07",
                    'NYSenatorRivera': "3.6615772014946863e-07",
                    'DrJayVarma':"3.5090114847657407e-07",
                    'rontkim': "2.7461829011210147e-07",
                    'JoshuaX1993': "2.2884857509341787e-07",
                    },
        closeness:{'realDonaldTrump': 0.019290448429499257,
                    'NYGovCuomo': 0.01054519781397903,
                    'nytimes': 0.007037585776668746,
                    'thehill': 0.005507397510265268,
                    'nypost': 0.0051410362327392895,
                    'CNN': 0.004978165938864629,
                    'DrEricDing': 0.004620965319655276,
                    'atrupar': 0.004333042212518195,
                    'MarkLevineNYC': 0.004215617223083064,
                    'kylegriffin1': 0.004104803493449782,
                    },
        indegree:{'realDonaldTrump': 0.019563318777292574,
                    'NYGovCuomo': 0.010480349344978166,
                    'nytimes': 0.007336244541484716,
                    'thehill': 0.005502183406113537,
                    'nypost': 0.005065502183406114,
                    'CNN': 0.004978165938864628,
                    'MarkLevineNYC': 0.004803493449781659,
                    'atrupar': 0.004279475982532751,
                    'kylegriffin1': 0.004104803493449782,
                    'AP': 0.003668122270742358,
                },
        outdegree:{'MerrylWiener': 0.012576419213973799,
                    'DrDiva82': 0.011441048034934497,
                    'Wildfang135': 0.007336244541484716,
                    'watergatesummer': 0.006986899563318777,
                    'AmBeautifulShow': 0.0053275109170305675,
                    'TimFullerton': 0.005240174672489083,
                    'ARaj_Energy': 0.0046288209606986895,
                    'jazza2z': 0.004192139737991266,
                    'TheMrJayBrown': 0.004104803493449782,
                    'jessepstein': 0.003580786026200873,
                    },
        betweeness2:{'MarkLevineNYC':" 7.369770108444061e-07",
                    'rafat': "4.737709355428325e-07",
                    'JuanMaBenitez':"4.211297204825178e-07",
                    'mattmfm': "2.105648602412589e-07",
                    'tomgara': "2.105648602412589e-07",
                    'DanMannarino': "2.105648602412589e-07",
                    'chefjoseandres': "2.105648602412589e-07",
                    'MarkTreyger718': "1.5792364518094417e-07",
                    'yuhline': "1.5792364518094417e-07",
                    'JustinBrannan': "1.5792364518094417e-07",
                    },
        closeness2:{'realDonaldTrump': 0.02081899518238128,
                    'NYGovCuomo': 0.013997676764366373,
                    'nytimes': 0.008029364533149804,
                    'thehill': 0.0077999541179169535,
                    'CNN': 0.006882312456985547,
                    'atrupar': 0.005047029135122735,
                    'NYCMayor': 0.004894088858300833,
                    'ABC': 0.004817618719889883,
                    'nypost': 0.004588208304657031,
                    'NBCNews': 0.003670566643725625,
                    },
        indegree2:{'realDonaldTrump': 0.02064693737095664,
                    'NYGovCuomo': 0.013994035329203946,
                    'nytimes': 0.008029364533149804,
                    'thehill': 0.0077999541179169535,
                    'CNN': 0.006882312456985546,
                    'atrupar': 0.005047029135122734,
                    'ABC': 0.004817618719889883,
                    'NYCMayor': 0.004817618719889883,
                    'nypost': 0.004588208304657031,
                    'NBCNews': 0.003670566643725625,
                },
        outdegree2:{'KevinClamato': 0.010552879100711171,
                    'ruthiecab': 0.010094058270245468,
                    'ARaj_Energy': 0.008488185363615508,
                    'humbertorosero': 0.007111722872218398,
                    'Ingridebap': 0.0066529020417526955,
                    'lastbohemians': 0.006423491626519844,
                    'mnutty': 0.005735260380821289,
                    'tummler10': 0.005735260380821289,
                    'LindseyBoylan': 0.005735260380821289,
                    'RonWaxman': 0.005276439550355586,
                    },



        betweeness3:{'gtconway3d': "1.276006832519617e-06",
                        'atrupar': "8.999206081980457e-07",
                        'mjs_DC':" 8.058990521176528e-07",
                        'AlexCTaliadoros': "5.238343838764744e-07",
                        'ReedReports':" 2.014747630294132e-07",
                        'PamKeithFL': "2.014747630294132e-07",
                        'CMLewisGeorgeW4': "1.8804311216078567e-07",
                        'aeidinger': "1.8804311216078567e-07",
                        'davidshepardson': "1.8804311216078567e-07",
                        'MinerPTO': "1.8804311216078567e-07",
                    },
        closeness3:{'realDonaldTrump': 0.016955143825826788,
                    'thehill': 0.007096057950860008,
                    'MayorBowser': 0.006403287548263792,
                    'washingtonpost': 0.004854665556948556,
                    'CNN': 0.0047736110049486765,
                    'nytimes': 0.004519643064086221,
                    'atrupar': 0.004030896824157164,
                    'JoeBiden': 0.003721301554190649,
                    'Reuters': 0.003620725836509821,
                    'NBCNews': 0.0031289836597519992,
                    },
        indegree3:{'realDonaldTrump': 0.01610847143353807,
                    'thehill': 0.007069185305365627,
                    'MayorBowser': 0.006489743886893035,
                    'washingtonpost': 0.004751419631475257,
                    'CNN': 0.004751419631475257,
                    'nytimes': 0.004519643064086221,
                    'atrupar': 0.004056089929308147,
                    'JoeBiden': 0.0037084250782245913,
                    'Reuters': 0.0035925367945300727,
                    'NBCNews': 0.003128983659751999,
                },
        outdegree3:{'Heerak4Congress': 0.06524510372001391,
                    'Dsquared75': 0.014370147178120291,
                    'LovelyLassSandy': 0.011588828369451848,
                    'PoeticLicencedk': 0.008228068142310812,
                    'richardmskinner': 0.007416850156449183,
                    'laurenskahn': 0.005678525901031405,
                    'twright55': 0.004635531347780739,
                    'HarlemGirl59': 0.004635531347780739,
                    'SimonWDC': 0.004056089929308147,
                    'JoJobeth328': 0.004056089929308147,
                    },
        

        
        betweeness4:{'atrupar': "3.155246986423603e-05",
                    'W7VOA': "6.41566887239466e-06",
                    'gtconway3d': "2.7345473882337893e-06",
                    'DanielleMisiak': "2.629372488686336e-06",
                    'falcicchio': "1.682798392759255e-06",
                    'MurielBowser': "1.5776234932118016e-06",
                    'albamonica': "1.2620987945694412e-06",
                    'chefjoseandres': "1.2620987945694412e-06",
                    'CalebJHull': "1.0517489954745343e-06",
                    'caroljoynt': "5.258744977372672e-07",
                    },
        closeness4:{'realDonaldTrump': 0.029231389850587743,
                    'MayorBowser': 0.008843296781039971,
                    'thehill': 0.007133592736705577,
                    'CNN': 0.00585278858625162,
                    'ABC': 0.005802080746198636,
                    'atrupar': 0.005206081567949272,
                    'Reuters': 0.005188067444876784,
                    'JoeBiden': 0.004559824902723736,
                    'NBCNews': 0.004539559014267186,
                    'AP': 0.004215304798962386,

                    },
        indegree4:{'realDonaldTrump': 0.028534370946822308,
                    'MayorBowser': 0.008754863813229572,
                    'thehill': 0.007133592736705577,
                    'CNN': 0.005836575875486381,
                    'atrupar': 0.005512321660181582,
                    'Reuters': 0.0048638132295719845,
                    'JoeBiden': 0.004539559014267185,
                    'NBCNews': 0.004539559014267185,
                    'AP': 0.004215304798962386,
                    'washingtonpost': 0.004215304798962386,
                },
        outdegree4:{'suzannelynch1': 0.013618677042801557,
                    'Dsquared75': 0.011673151750972763,
                    'cdorobek': 0.00940337224383917,
                    'therockyfiles': 0.00940337224383917,
                    'miketheidealist': 0.00907911802853437,
                    'sanambna': 0.008430609597924773,
                    'funkyartist': 0.008106355382619973,
                    'KelseyDuckett': 0.008106355382619973,
                    'New_Columbia': 0.006809338521400778,
                    'Aly_Dar8': 0.006485084306095979,
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
