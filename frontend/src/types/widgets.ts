// Define an interface for the widgets JSON object
export interface Article {
    title: string;
    source: string;
    date: string;
    link: string;
    description: string;
}

export interface Widget {
    searchTerm: string;
    numberOfDays: number;
    articles: Article[];
}

export interface WidgetsJSON {
    widgets: Widget[];
}

// Example of this JSON Object:

// var newWidgetsObj: WidgetsJSON = {
//     widgets: [
//       {
//         searchTerm: "Northeastern University",
//         numberOfDays: 30,
//         articles: [
//           {
//             title: "NU-Title1",
//             source: "NU-Source1",
//             date: "NU-Date1",
//             link: "NU-Link1",
//             description: "blah blah blah"
//           },
//           {
//             title: "NU-Title2",
//             source: "NU-Source2",
//             date: "NU-Date2",
//             link: "NU-Link2",
//             description: "blah blah blah"
//           },
//           {
//             title: "NU-Title3",
//             source: "NU-Source3",
//             date: "NU-Date3",
//             link: "NU-Link3",
//             description: "blah blah blah"
//           }
//         ]
//       },
//       {
//         searchTerm: "Katherine Docks",
//         numberOfDays: 7,
//         articles: [
//           {
//             title: "KD-Title1",
//             source: "KD-Source1",
//             date: "KD-Date1",
//             link: "KD-Link1",
//             description: "blah blah blah"
//           },
//           {
//             title: "KD-Title2",
//             source: "KD-Source2",
//             date: "KD-Date2",
//             link: "KD-Link2",
//             description: "blah blah blah"
//           },
//           {
//             title: "KD-Title3",
//             source: "KD-Source3",
//             date: "KD-Date3",
//             link: "KD-Link3",
//             description: "blah blah blah"
//           }
//         ]
//       },
//       {
//         searchTerm: "England Cricket",
//         numberOfDays: 90,
//         articles: [
//           {
//             title: "EC-Title1",
//             source: "EC-Source1",
//             date: "EC-Date1",
//             link: "EC-Link1",
//             description: "blah blah blah"
//           },
//           {
//             title: "EC-Title2",
//             source: "EC-Source2",
//             date: "EC-Date2",
//             link: "EC-Link2",
//             description: "blah blah blah"
//           },
//           {
//             title: "EC-Title3",
//             source: "EC-Source3",
//             date: "EC-Date3",
//             link: "EC-Link3",
//             description: "blah blah blah"
//           }
//         ]
//       }
//     ]
// }