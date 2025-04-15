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
        document.querySelectorAll("#bGmlqc").forEach(sponsorLink => sponsorLink.remove()); //sponsorLinks
        document.querySelectorAll(".uEierd").forEach(sponsorLink => sponsorLink.remove()); //sponsorLinks
        document.querySelectorAll("[data-hveid='uEierd']").forEach(fastPickupDelivery => fastPickupDelivery.remove()); //fastPickupDelivery
        document.querySelectorAll(".mnr-c.sPmWM").forEach(buyingGuild => buyingGuild.remove()); //buyingGuild
        document.querySelectorAll(".cUnQKe").forEach(peopleAlsoAsk => peopleAlsoAsk.remove()); //peopleAlsoAsk
        document.querySelectorAll("[data-hveid='CCYQAA']").forEach(exploreBrands => exploreBrands.remove()); //exploreBrands
        document.querySelectorAll("[data-hveid='CFEQAA']").forEach(peopleAlsoBuyFrom => peopleAlsoBuyFrom.remove()); //peopleAlsoBuyFrom
        document.querySelectorAll(".oIk2Cb").forEach(peopleAlsoSearchFor => peopleAlsoSearchFor.remove()); //peopleAlsoSearchFor

        document.querySelectorAll('g-card[class="T98FId"]').forEach( AdditionlCatergories => AdditionlCatergories.remove() ); // Additional catergories
        document.querySelectorAll('h3.LC20lb.MBeuO.DKV0Md').forEach( function(header) {header.append(' 💀')} ); // for adding website rating
        document.querySelectorAll('.Yt787').forEach( function(header) {header.append(' 💀')} ); //images headers
        
    }
    // document.querySelector('#bGmlqc').remove();
    // document.querySelector('.uEierd').remove();
    // document.querySelector('g-card[class="T98FId"]').remove(); // Additional catergories

});
 