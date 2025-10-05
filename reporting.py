"""
Comprehensive Reporting Module
Produces clear and concise reports in Markdown, PDF, and spreadsheet formats
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
import pandas as pd
from jinja2 import Template
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import logging
import markdown
from weasyprint import HTML, CSS
import io
import base64

logger = logging.getLogger(__name__)

@dataclass
class ReportConfig:
    """Configuration for report generation"""
    title: str
    subtitle: Optional[str] = None
    author: str = "Research & Analysis Agent"
    company: str = "Research Agency"
    format: str = "markdown"  # markdown, pdf, html, excel
    template: str = "default"
    include_charts: bool = True
    include_tables: bool = True
    include_sources: bool = True
    page_size: str = "A4"
    font_size: int = 12
    color_scheme: str = "professional"

@dataclass
class ReportSection:
    """Represents a section of a report"""
    title: str
    content: str
    level: int = 1  # Heading level
    subsections: List['ReportSection'] = None
    charts: List[Dict[str, Any]] = None
    tables: List[Dict[str, Any]] = None

class ReportGenerator:
    """Comprehensive report generation engine"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
        # Report templates
        self.templates = {
            'default': self._get_default_template(),
            'executive': self._get_executive_template(),
            'technical': self._get_technical_template(),
            'market': self._get_market_template()
        }
        
        # Color schemes
        self.color_schemes = {
            'professional': {
                'primary': '#2C3E50',
                'secondary': '#3498DB',
                'accent': '#E74C3C',
                'text': '#2C3E50',
                'background': '#FFFFFF'
            },
            'corporate': {
                'primary': '#1A365D',
                'secondary': '#3182CE',
                'accent': '#E53E3E',
                'text': '#1A202C',
                'background': '#F7FAFC'
            },
            'modern': {
                'primary': '#1A202C',
                'secondary': '#4299E1',
                'accent': '#F56565',
                'text': '#2D3748',
                'background': '#FFFFFF'
            }
        }
    
    def generate_report(self, structured_data: Dict[str, Any], 
                       report_config: ReportConfig) -> str:
        """
        Generate comprehensive report
        
        Args:
            structured_data: Structured research data
            report_config: Report configuration
            
        Returns:
            Path to generated report file
        """
        logger.info(f"Generating {report_config.format} report: {report_config.title}")
        
        # Create report sections
        sections = self._create_report_sections(structured_data, report_config)
        
        # Generate report based on format
        if report_config.format.lower() == 'markdown':
            return self._generate_markdown_report(sections, report_config)
        elif report_config.format.lower() == 'pdf':
            return self._generate_pdf_report(sections, report_config)
        elif report_config.format.lower() == 'html':
            return self._generate_html_report(sections, report_config)
        elif report_config.format.lower() == 'excel':
            return self._generate_excel_report(structured_data, report_config)
        else:
            raise ValueError(f"Unsupported report format: {report_config.format}")
    
    def generate_executive_summary(self, structured_data: Dict[str, Any]) -> str:
        """
        Generate executive summary
        
        Args:
            structured_data: Structured research data
            
        Returns:
            Executive summary text
        """
        logger.info("Generating executive summary")
        
        summary_parts = []
        
        # Extract key metrics
        if 'market_share' in structured_data:
            total_companies = len(structured_data['market_share'])
            leader = max(structured_data['market_share'], 
                       key=structured_data['market_share'].get)
            leader_share = structured_data['market_share'][leader]
            summary_parts.append(
                f"The market analysis covers {total_companies} companies, "
                f"with {leader} leading at {leader_share}% market share."
            )
        
        if 'trends' in structured_data:
            trend_count = len(structured_data['trends'])
            high_growth_trends = len([t for t in structured_data['trends'] 
                                   if t.get('growth_rate', 0) > 30])
            summary_parts.append(
                f"Analysis identified {trend_count} significant trends, "
                f"with {high_growth_trends} showing high growth potential."
            )
        
        if 'competitors' in structured_data:
            competitor_count = len(structured_data['competitors'])
            summary_parts.append(
                f"Competitive landscape analysis includes {competitor_count} "
                f"key market players."
            )
        
        # Add strategic insights
        summary_parts.extend([
            "Key opportunities include early adoption of emerging technologies and strategic partnerships.",
            "Market consolidation is expected to continue, creating opportunities for market leaders.",
            "Technology innovation remains a critical differentiator in competitive positioning."
        ])
        
        return " ".join(summary_parts)
    
    def generate_market_brief(self, market_data: Dict[str, Any]) -> str:
        """
        Generate market brief report
        
        Args:
            market_data: Market analysis data
            
        Returns:
            Path to generated market brief
        """
        logger.info("Generating market brief")
        
        config = ReportConfig(
            title=f"Market Brief: {market_data.get('industry', 'Market Analysis')}",
            subtitle="Strategic Market Intelligence Report",
            format="pdf",
            template="market"
        )
        
        return self.generate_report(market_data, config)
    
    def generate_competitive_intelligence_report(self, competitive_data: Dict[str, Any]) -> str:
        """
        Generate competitive intelligence report
        
        Args:
            competitive_data: Competitive analysis data
            
        Returns:
            Path to generated report
        """
        logger.info("Generating competitive intelligence report")
        
        config = ReportConfig(
            title=f"Competitive Intelligence: {competitive_data.get('industry', 'Industry')}",
            subtitle="Comprehensive Competitive Analysis",
            format="pdf",
            template="executive"
        )
        
        return self.generate_report(competitive_data, config)
    
    def generate_trend_report(self, trend_data: Dict[str, Any]) -> str:
        """
        Generate trend analysis report
        
        Args:
            trend_data: Trend analysis data
            
        Returns:
            Path to generated trend report
        """
        logger.info("Generating trend analysis report")
        
        config = ReportConfig(
            title=f"Trend Analysis: {trend_data.get('topic', 'Market Trends')}",
            subtitle="Emerging Trends and Market Opportunities",
            format="markdown",
            template="technical"
        )
        
        return self.generate_report(trend_data, config)
    
    def _create_report_sections(self, structured_data: Dict[str, Any], 
                               config: ReportConfig) -> List[ReportSection]:
        """Create report sections from structured data"""
        sections = []
        
        # Executive Summary
        executive_summary = self.generate_executive_summary(structured_data)
        sections.append(ReportSection(
            title="Executive Summary",
            content=executive_summary,
            level=1
        ))
        
        # Market Overview
        if 'market_share' in structured_data or 'industry' in structured_data:
            market_content = self._generate_market_overview_content(structured_data)
            sections.append(ReportSection(
                title="Market Overview",
                content=market_content,
                level=1
            ))
        
        # Competitive Analysis
        if 'competitors' in structured_data:
            competitive_content = self._generate_competitive_content(structured_data)
            sections.append(ReportSection(
                title="Competitive Analysis",
                content=competitive_content,
                level=1
            ))
        
        # Trend Analysis
        if 'trends' in structured_data:
            trend_content = self._generate_trend_content(structured_data)
            sections.append(ReportSection(
                title="Trend Analysis",
                content=trend_content,
                level=1
            ))
        
        # Key Insights
        if 'key_insights' in structured_data:
            insights_content = self._generate_insights_content(structured_data)
            sections.append(ReportSection(
                title="Key Insights",
                content=insights_content,
                level=1
            ))
        
        # Recommendations
        if 'recommendations' in structured_data:
            recommendations_content = self._generate_recommendations_content(structured_data)
            sections.append(ReportSection(
                title="Strategic Recommendations",
                content=recommendations_content,
                level=1
            ))
        
        # Sources
        if config.include_sources and 'sources' in structured_data:
            sources_content = self._generate_sources_content(structured_data)
            sections.append(ReportSection(
                title="Sources",
                content=sources_content,
                level=1
            ))
        
        return sections
    
    def _generate_markdown_report(self, sections: List[ReportSection], 
                                 config: ReportConfig) -> str:
        """Generate Markdown format report"""
        filename = f"{config.title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.md"
        
        markdown_content = []
        
        # Header
        markdown_content.append(f"# {config.title}")
        if config.subtitle:
            markdown_content.append(f"## {config.subtitle}")
        
        markdown_content.append(f"**Author:** {config.author}")
        markdown_content.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d')}")
        markdown_content.append("")
        
        # Sections
        for section in sections:
            markdown_content.append(f"{'#' * section.level} {section.title}")
            markdown_content.append("")
            markdown_content.append(section.content)
            markdown_content.append("")
            
            # Add subsections
            if section.subsections:
                for subsection in section.subsections:
                    markdown_content.append(f"{'#' * (subsection.level + 1)} {subsection.title}")
                    markdown_content.append("")
                    markdown_content.append(subsection.content)
                    markdown_content.append("")
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(markdown_content))
        
        return filename
    
    def _generate_pdf_report(self, sections: List[ReportSection], 
                           config: ReportConfig) -> str:
        """Generate PDF format report"""
        filename = f"{config.title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        doc = SimpleDocTemplate(filename, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor(self.color_schemes[config.color_scheme]['primary'])
        )
        
        story.append(Paragraph(config.title, title_style))
        
        if config.subtitle:
            subtitle_style = ParagraphStyle(
                'CustomSubtitle',
                parent=styles['Heading2'],
                fontSize=14,
                spaceAfter=20,
                alignment=TA_CENTER,
                textColor=colors.HexColor(self.color_schemes[config.color_scheme]['secondary'])
            )
            story.append(Paragraph(config.subtitle, subtitle_style))
        
        # Author and date
        info_style = ParagraphStyle(
            'Info',
            parent=styles['Normal'],
            fontSize=10,
            alignment=TA_CENTER,
            spaceAfter=30
        )
        story.append(Paragraph(f"Author: {config.author}", info_style))
        story.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", info_style))
        story.append(Spacer(1, 20))
        
        # Sections
        for section in sections:
            # Section title
            if section.level == 1:
                section_style = ParagraphStyle(
                    'SectionTitle',
                    parent=styles['Heading1'],
                    fontSize=14,
                    spaceAfter=12,
                    spaceBefore=20,
                    textColor=colors.HexColor(self.color_schemes[config.color_scheme]['primary'])
                )
            else:
                section_style = ParagraphStyle(
                    'SubsectionTitle',
                    parent=styles['Heading2'],
                    fontSize=12,
                    spaceAfter=8,
                    spaceBefore=12,
                    textColor=colors.HexColor(self.color_schemes[config.color_scheme]['secondary'])
                )
            
            story.append(Paragraph(section.title, section_style))
            
            # Section content
            content_style = ParagraphStyle(
                'Content',
                parent=styles['Normal'],
                fontSize=config.font_size,
                spaceAfter=6,
                alignment=TA_LEFT
            )
            
            # Split content into paragraphs
            paragraphs = section.content.split('\n\n')
            for para in paragraphs:
                if para.strip():
                    story.append(Paragraph(para.strip(), content_style))
                    story.append(Spacer(1, 6))
            
            story.append(Spacer(1, 12))
        
        # Build PDF
        doc.build(story)
        
        return filename
    
    def _generate_html_report(self, sections: List[ReportSection], 
                            config: ReportConfig) -> str:
        """Generate HTML format report"""
        filename = f"{config.title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.html"
        
        html_content = []
        
        # HTML header
        colors = self.color_schemes[config.color_scheme]
        html_content.append(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{config.title}</title>
            <meta charset="utf-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: {colors['text']};
                    background-color: {colors['background']};
                    margin: 40px;
                }}
                h1 {{
                    color: {colors['primary']};
                    border-bottom: 2px solid {colors['secondary']};
                    padding-bottom: 10px;
                }}
                h2 {{
                    color: {colors['secondary']};
                    margin-top: 30px;
                }}
                h3 {{
                    color: {colors['accent']};
                }}
                .header {{
                    text-align: center;
                    margin-bottom: 40px;
                }}
                .meta {{
                    font-size: 12px;
                    color: #666;
                    text-align: center;
                    margin-bottom: 30px;
                }}
            </style>
        </head>
        <body>
        """)
        
        # Header
        html_content.append('<div class="header">')
        html_content.append(f'<h1>{config.title}</h1>')
        if config.subtitle:
            html_content.append(f'<h2>{config.subtitle}</h2>')
        html_content.append('</div>')
        
        # Meta information
        html_content.append('<div class="meta">')
        html_content.append(f'<p>Author: {config.author} | Date: {datetime.now().strftime("%Y-%m-%d")}</p>')
        html_content.append('</div>')
        
        # Sections
        for section in sections:
            html_content.append(f'<h{section.level}>{section.title}</h{section.level}>')
            html_content.append(f'<p>{section.content}</p>')
        
        html_content.append('</body></html>')
        
        # Write to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_content))
        
        return filename
    
    def _generate_excel_report(self, structured_data: Dict[str, Any], 
                             config: ReportConfig) -> str:
        """Generate Excel format report"""
        filename = f"{config.title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.xlsx"
        
        with pd.ExcelWriter(filename, engine='openpyxl') as writer:
            # Summary sheet
            summary_data = {
                'Metric': ['Title', 'Author', 'Date', 'Industry', 'Analysis Type'],
                'Value': [
                    config.title,
                    config.author,
                    datetime.now().strftime('%Y-%m-%d'),
                    structured_data.get('industry', 'N/A'),
                    'Comprehensive Analysis'
                ]
            }
            summary_df = pd.DataFrame(summary_data)
            summary_df.to_excel(writer, sheet_name='Summary', index=False)
            
            # Market share sheet
            if 'market_share' in structured_data:
                market_share_data = [
                    {'Company': company, 'Market Share (%)': share}
                    for company, share in structured_data['market_share'].items()
                ]
                market_share_df = pd.DataFrame(market_share_data)
                market_share_df.to_excel(writer, sheet_name='Market Share', index=False)
            
            # Competitors sheet
            if 'competitors' in structured_data:
                competitors_df = pd.DataFrame(structured_data['competitors'])
                competitors_df.to_excel(writer, sheet_name='Competitors', index=False)
            
            # Trends sheet
            if 'trends' in structured_data:
                trends_df = pd.DataFrame(structured_data['trends'])
                trends_df.to_excel(writer, sheet_name='Trends', index=False)
            
            # Insights sheet
            if 'key_insights' in structured_data:
                insights_df = pd.DataFrame({
                    'Key Insights': structured_data['key_insights']
                })
                insights_df.to_excel(writer, sheet_name='Insights', index=False)
            
            # Recommendations sheet
            if 'recommendations' in structured_data:
                recommendations_df = pd.DataFrame({
                    'Recommendations': structured_data['recommendations']
                })
                recommendations_df.to_excel(writer, sheet_name='Recommendations', index=False)
        
        return filename
    
    def _generate_market_overview_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate market overview content"""
        content_parts = []
        
        if 'industry' in structured_data:
            content_parts.append(f"The {structured_data['industry']} industry represents a significant market opportunity.")
        
        if 'market_share' in structured_data:
            total_companies = len(structured_data['market_share'])
            content_parts.append(f"Market analysis covers {total_companies} key players.")
            
            # Market concentration analysis
            shares = list(structured_data['market_share'].values())
            top_3_share = sum(sorted(shares, reverse=True)[:3])
            content_parts.append(f"Top 3 companies control {top_3_share:.1f}% of the market.")
        
        if 'market_size' in structured_data:
            market_size = structured_data['market_size']
            content_parts.append(f"Total market size is estimated at ${market_size:,.0f}.")
        
        return " ".join(content_parts)
    
    def _generate_competitive_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate competitive analysis content"""
        content_parts = []
        
        if 'competitors' in structured_data:
            competitor_count = len(structured_data['competitors'])
            content_parts.append(f"Competitive analysis includes {competitor_count} major players.")
            
            # Analyze competitive positioning
            if 'competitive_positioning' in structured_data:
                positioning = structured_data['competitive_positioning']
                leaders = [comp for comp, pos in positioning.items() if pos == 'Market Leader']
                if leaders:
                    content_parts.append(f"Market leaders include: {', '.join(leaders)}.")
        
        if 'key_differentiators' in structured_data:
            content_parts.append("Key competitive differentiators include innovation, market reach, and customer service.")
        
        return " ".join(content_parts)
    
    def _generate_trend_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate trend analysis content"""
        content_parts = []
        
        if 'trends' in structured_data:
            trend_count = len(structured_data['trends'])
            content_parts.append(f"Analysis identified {trend_count} significant trends.")
            
            # High growth trends
            high_growth = [t for t in structured_data['trends'] if t.get('growth_rate', 0) > 30]
            if high_growth:
                content_parts.append(f"{len(high_growth)} trends show high growth potential (>30%).")
            
            # Early adoption trends
            early_trends = [t for t in structured_data['trends'] 
                          if t.get('adoption_level') in ['innovator', 'early_adopter']]
            if early_trends:
                content_parts.append(f"{len(early_trends)} trends are in early adoption phase.")
        
        return " ".join(content_parts)
    
    def _generate_insights_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate key insights content"""
        if 'key_insights' in structured_data:
            insights = structured_data['key_insights']
            return " ".join([f"• {insight}" for insight in insights])
        return "Key insights will be generated based on comprehensive analysis."
    
    def _generate_recommendations_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate recommendations content"""
        if 'recommendations' in structured_data:
            recommendations = structured_data['recommendations']
            return " ".join([f"• {rec}" for rec in recommendations])
        return "Strategic recommendations will be provided based on analysis findings."
    
    def _generate_sources_content(self, structured_data: Dict[str, Any]) -> str:
        """Generate sources content"""
        if 'sources' in structured_data:
            sources = structured_data['sources']
            return "\n".join([f"• {source}" for source in sources])
        return "Sources will be listed upon completion of research."
    
    def _get_default_template(self) -> str:
        """Get default report template"""
        return """
        # {{ title }}
        
        ## Executive Summary
        {{ executive_summary }}
        
        ## Market Overview
        {{ market_overview }}
        
        ## Competitive Analysis
        {{ competitive_analysis }}
        
        ## Trend Analysis
        {{ trend_analysis }}
        
        ## Key Insights
        {{ key_insights }}
        
        ## Recommendations
        {{ recommendations }}
        
        ## Sources
        {{ sources }}
        """
    
    def _get_executive_template(self) -> str:
        """Get executive summary template"""
        return """
        # {{ title }}
        
        ## Executive Summary
        {{ executive_summary }}
        
        ## Strategic Recommendations
        {{ recommendations }}
        
        ## Key Market Insights
        {{ key_insights }}
        """
    
    def _get_technical_template(self) -> str:
        """Get technical analysis template"""
        return """
        # {{ title }}
        
        ## Methodology
        {{ methodology }}
        
        ## Data Analysis
        {{ data_analysis }}
        
        ## Technical Findings
        {{ technical_findings }}
        
        ## Detailed Analysis
        {{ detailed_analysis }}
        """
    
    def _get_market_template(self) -> str:
        """Get market analysis template"""
        return """
        # {{ title }}
        
        ## Market Overview
        {{ market_overview }}
        
        ## Market Size and Growth
        {{ market_size }}
        
        ## Competitive Landscape
        {{ competitive_landscape }}
        
        ## Market Opportunities
        {{ market_opportunities }}
        
        ## Market Challenges
        {{ market_challenges }}
        """
