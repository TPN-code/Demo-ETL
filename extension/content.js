console.log("%c[Preload] Script running before page loads!", "color: green; font-weight: bold;");

// Example: Block all images from loading
document.addEventListener("DOMContentLoaded", () => {
    let mainURL = location.href.toString()
    if (mainURL.includes("www.google.com")) {
        let hrefLinks = document.querySelectorAll('a');
        let domainList = [];
        hrefLinks.forEach(link => {
            var hrefStr = link.href.toString();
            if (hrefStr !== '' && !hrefStr.includes(".google.com/")) {
                var domain = hrefStr.split('/').slice(0, 3).join('/') + '/';
                if (!domainList.includes(domain)) {
                    domainList.push(domain);
                };
            };
        });
        console.log(domainList);
        // document.querySelectorAll('h3.LC20lb.MBeuO.DKV0Md').forEach( function(header) {header.append(' 💀')} ); // for adding website rating
        // document.querySelectorAll('.Yt787').forEach( function(header) {header.append(' 💀')} ); //images headers


        //All
        //https://www.google.com/search?q=laptop+14&sca_esv=fe1053e518bd0343&ei=sa_-Z_b7PObS5NoPm7-2-Ac&start=0&sa=N&sstk=Af40H4Xpy0D3bmse37l5CmrVVgfD2oyBEG3efFIvoFrR2TGN3H8Jna8AKkU7f9x6vlLPKn2Q9MR2ugmWuSpqjM8qOhd7bNjD3tJ60c6MW_AOP3oabwy2CL2SL_c22_03KlNx&ved=2ahUKEwi2mJej39qMAxVmKVkFHZufDX84FBDy0wN6BAgIEAQ&biw=1449&bih=1094&dpr=0.83
        if (mainURL.includes("search?q=")) {
            document.querySelectorAll(".c3mZkd.cu-container").forEach(sponsorLink => sponsorLink.remove()); //sponsorLinks
            document.querySelectorAll("#Odp5De").forEach(mainSearch => mainSearch.remove()); //mainSearch
            document.querySelectorAll(".cUnQKe").forEach(peopleAlsoAsk => peopleAlsoAsk.remove()); //peopleAlsoAsk
            document.querySelectorAll(".ULSxyf.yhQgZb").forEach(WEPP => WEPP.remove()); //whatPeopleAreSaying exploreBrands peopleAlsoBuyFrom peopleAlsoSearchFor
            document.querySelectorAll(".NPn0Pb").forEach(fastPickupDelivery => fastPickupDelivery.remove()); //fastPickupDelivery
            document.querySelectorAll(".f8O9Qd.NPn0Pb").forEach(inStoreNearBy => inStoreNearBy.remove()); //inStoreNearBy
            document.querySelectorAll(".mnr-c.sPmWM").forEach(buyingGuild => buyingGuild.remove()); //buyingGuild
            document.querySelectorAll(".baPFxb.kSMK2.wHYlTd.Nt5hrb").forEach(popularProducts => popularProducts.remove()); //PopularProducts
        }

        //shopping
        //https://www.google.com/search?sca_esv=fe1053e518bd0343&q=laptop+14&udm=28&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqengxVrJ7hrmYmz7X2OZp_NIei751D_uHp6okcxWX5B7wTtpupFUv3gevgjN2RZ8PFpKxWH_YAcfhz7SXMXuXdDDGnGkSzfBc201WqFVOBuCuigGosndHwzZa6JIVWHcKhbONG0_G-AqDuh7lTKO9GIB3fSMYw&ved=1t:220175&ictx=111&biw=1449&bih=1094&dpr=0.83#ip=1
        if(mainURL.includes("search?sca_esv=")) {
            document.querySelectorAll(".DUkiH.cu-container").forEach(sponsorLink => sponsorLink.remove()); //sponsorLinks - Shopping
        }

        //Images
        // https://www.google.com/search?sca_esv=fe1053e518bd0343&biw=1449&bih=1094&q=laptop+14&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0fn3xuWpA-dk4wpBWOGsoR7DG5zJBsxayPSIAqObp_AgjkUGqengxVrJ7hrmYmz7X2OZp_NIei751D_uHp6okcxWX5B7wTtpupFUv3gevgjN2RZ8PFpKxWH_YAcfhz7SXMXuXdDDGnGkSzfBc201WqFVOBuCuigGosndHwzZa6JIVWHcKhbONG0_G-AqDuh7lTKO9GIB3fSMYw&sa=X&ved=2ahUKEwi9xKDE39qMAxW_K1kFHVghDc8QtKgLegQIFBAB
        if(mainURL.includes("search?sca_esv=")) {
            document.querySelectorAll(".DUkiH.cu-container").forEach(sponsorLink => sponsorLink.remove()); //sponsorLinks - Images
        }
        
    }

});
 